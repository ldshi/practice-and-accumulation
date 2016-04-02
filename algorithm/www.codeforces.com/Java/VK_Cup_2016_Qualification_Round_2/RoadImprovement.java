/*
 * Compiler info given out by 'java -version':
 *   java version "1.8.0_66"
 *   Java(TM) SE Runtime Environment (build 1.8.0_66-b17)
 *   Java HotSpot(TM) 64-Bit Server VM (build 25.66-b17, mixed mode)
 */

import java.io.IOException;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;

public class RoadImprovement {

  private static ArrayList<ArrayList<ArrayList<String>>> accumulation = new ArrayList<ArrayList<ArrayList<String>>>();

  private static void addSibling(String roadNumber, String roadBegin, String roadEnd) {
    ArrayList<ArrayList<String>> siblings = new ArrayList<ArrayList<String>>();
    ArrayList<String> roads = new ArrayList<String>(Arrays.asList(roadNumber));
    ArrayList<String> roadNodes = new ArrayList<String>(Arrays.asList(roadBegin, roadEnd));
    
    siblings.add(roads);
    siblings.add(roadNodes);
    accumulation.add(siblings);
  }

  private static void accumulator(String roadNumber, String roadBegin, String roadEnd) {
    if (accumulation.size() == 0) {
      addSibling(roadNumber, roadBegin, roadEnd);

      return;
    }

    //
    // Haha, can't return the method from inside the lambda!!!
    // Refer to the below link for understanding 'Stream.forEach' better:
    //   http://stackoverflow.com/questions/23996454/terminate-or-break-java-8-stream-loop
    //
    // accumulation.forEach((item) -> {
    //   if (!item.get(1).contains(roadBegin) && !item.get(1).contains(roadEnd)) {
    //     item.get(0).add(roadNumber);
    //     item.get(1).add(roadBegin);
    //     item.get(1).add(roadEnd);

    //     return;
    //   }
    // });

    // So, lets go back to the traditional one.
    for (int i = 0; i < accumulation.size(); i++) {
      if (!accumulation.get(i).get(1).contains(roadBegin) && !accumulation.get(i).get(1).contains(roadEnd)) {
        accumulation.get(i).get(0).add(roadNumber);
        accumulation.get(i).get(1).add(roadBegin);
        accumulation.get(i).get(1).add(roadEnd);

        return;
      }
    }

    addSibling(roadNumber, roadBegin, roadEnd);
  }

  public static void main(String[] args) {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int cityAmount = 0, roadNumber = -1;

    while (roadNumber < cityAmount) {
      if (roadNumber == -1) {
        while (true) {
          String str = null;

          try {
            str = br.readLine();
          } catch (IOException e) {
            e.printStackTrace();
          }

          if (str != null) {
            cityAmount = Integer.parseInt(str.trim());
            roadNumber = 1;

            break;
          }
        }
      } else {
        String str = null;

        try {
          str = br.readLine();
        } catch (IOException e) {
          e.printStackTrace();
        }

        if (str != null) {
          String[] roadNodes = str.split(" ");
          accumulator(String.valueOf(roadNumber), roadNodes[0], roadNodes[1]);
          roadNumber++;
        }
      }
    }

    System.out.println(accumulation.size());
    accumulation.forEach((item) -> {
      System.out.println(String.valueOf(item.get(0).size()) + " " + String.join(" ", item.get(0)));
    });

  }

}


