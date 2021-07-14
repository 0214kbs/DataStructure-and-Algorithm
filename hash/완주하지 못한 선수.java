/* 프로그래머스 해시 Lv 1 - 완주하지 못한 선수
 https://programmers.co.kr/learn/courses/30/lessons/42576 */

/* 문제 해설
https://bskwak.tistory.com/222 참고 
 */
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        HashMap<String,Integer> hm = new HashMap<>();
        String answer = "";
        
        for(String player : participant) 
            hm.put(player,hm.getOrDefault(player,0)+1);
        
        for(String player : completion) 
            hm.put(player,hm.get(player)-1);
        
        for(String key : hm.keySet())
            if(hm.get(key)!=0){
                answer = key;
                System.out.println(answer);
            }
        return answer;
    }
}
