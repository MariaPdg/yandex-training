def bench_legs_to_leave(length, coord):

     if length % 2 and length // 2 in coord:
          return [length // 2]

     l = length // 2 - 1
     r = l + 1
     res = []
     while l >= 0:
          if l in coord:
               res.append(l)
               break
          l -= 1
     while r < length:
          if r in coord:
               res.append(r)
               break
          r += 1

     return res


if __name__ == '__main__':

     """ Input: l = length of a bench, k = number of legs, coord = location of legs.
         Output: location of legs, which should be left.
         Condition: at least one leg in the left and right sides from the bench center."""

     l, k = map(int, input().split())
     coord = [int(x) for x in input().split()]
     res = bench_legs_to_leave(l, coord)
     print(*res)
