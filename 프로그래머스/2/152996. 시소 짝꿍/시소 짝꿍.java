import java.util.*;

class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        Map<Double, Integer> map = new HashMap<>();

        Arrays.sort(weights);

        for (int w : weights) {
            double[] ratios = {
                w * 1.0,
                w * 2.0 / 3,
                w * 1.0 / 2,
                w * 3.0 / 4
            };

            for (double r : ratios) {
                if (map.containsKey(r)) {
                    answer += map.get(r);
                }
            }

            map.put(w * 1.0, map.getOrDefault(w * 1.0, 0) + 1);
        }

        return answer;
    }
}
