import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        if (x == y) return 0;

        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[y + 1];
        q.add(new int[]{x, 0});
        visited[x] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();
            int cur = now[0];
            int cnt = now[1];

            int[] nexts = {cur + n, cur * 2, cur * 3};

            for (int next : nexts) {
                if (next > y || visited[next]) continue;
                if (next == y) return cnt + 1;
                visited[next] = true;
                q.add(new int[]{next, cnt + 1});
            }
        }

        return -1;
    }
}
