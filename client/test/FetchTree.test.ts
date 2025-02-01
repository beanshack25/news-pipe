import { expect, test } from 'vitest';
import { apiResponseToTree } from '../src/lib/familytree/fetchTree';
import { People } from '../src/lib/familytree/models';

const basicPersonData = (id: string, depth: number) => ({
  data: {
    id,
    name: id,
    gender: 'prefer not to say' as const
  },
  id,
  depth
});

test('Handles two marriages with different children', () => {
  const resultingPeople: People = [];

  for (const { id, depth } of [
    { id: 'Wife 1', depth: 1 },
    { id: 'Child 1', depth: 2 },
    { id: 'Wife 2', depth: 1 },
    { id: 'Child 2', depth: 2 },
    { id: 'Focus', depth: 1 }
  ]) {
    resultingPeople.push([id, { name: id }]);
  }

  const result = apiResponseToTree({
    root: basicPersonData('Focus', 1),
    nodes: [
      basicPersonData('Focus', 1),
      basicPersonData('Wife 1', 1),
      basicPersonData('Child 1', 2),
      basicPersonData('Wife 2', 1),
      basicPersonData('Child 2', 2)
    ],
    edges: [
      {
        node1: 'Focus',
        node2: 'Wife 1'
      },
      {
        node1: 'Focus',
        node2: 'Wife 2'
      },
      {
        node1: 'Focus',
        node2: 'Child 1'
      },
      {
        node1: 'Wife 1',
        node2: 'Child 1'
      },
      {
        node1: 'Focus',
        node2: 'Child 2'
      },
      {
        node1: 'Wife 2',
        node2: 'Child 2'
      }
    ]
  });

  expect(result.focus).toBe('Focus');
  expect(new Map(result.people)).toStrictEqual(new Map(resultingPeople));
  expect(new Set(result.marriages)).toStrictEqual(
    new Set([
      { parents: ['Focus', 'Wife 1'], children: ['Child 1'] },
      { parents: ['Focus', 'Wife 2'], children: ['Child 2'] }
    ])
  );
});
