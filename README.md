## Description
- This repository is for recording all kinds of the daily practice and accumulation.

## Accumulations / References
1. Find out the length of the longest path and one possible longest path in a multi-way tree
  - Required tree description example: {5: {0: [6, 7], 1: [9, 0], 2: [4], 5: [1], 6: [3, 8], 7: [2]}}
    - '5' is root
    - '{0: [6, 7], 1: [9, 0], 2: [4], 5: [1], 6: [3, 8], 7: [2]}' is paths descriptions
  - Source code and explanation refer to: [high_speed_camera_cover.py -> find_longest_road(tree, root)](algorithm/codility.com/20160330/high_speed_camera_cover/high_speed_camera_cover.py)
  
2. [SQL various of 'join', 'group by' and 'having' understanding](sql/README.20160401.basic.md)
  - When proceed the join operation, if two tables have the same column, then some SQL product will use the later one override the previous one.
    - So:
      - **Never use '*' in the 'select', this is a very important good practice.**
      - **If two tables have same columns, then rename them use 'as' in 'select' will get around of this problem.**
  
  - 'group by' and 'having'
    - The 'group by' statement will proceed the 'group operation' by the condition given by you after the 'by' and form the records into several groups, then proceed the 'having conditions' on **EACH GROUP, here you should pay enough attention to _EACH GROUP_, not: proceed 'having conditions' on those records inside each group, but _EACH GROUP_, that means only having two results:**
          - **Keep this group.**
          - **Omit this group.**
          - **As how to choose one record from those kept groups, and then form into the output, you told no clue to SQL how to do that, so probably it depends on how SQL throws the dice.**
          - So:
            - **Here require you to make all the records inside a group are same in a sense to your query, that is: choosing which record as reference doesn't matter.**
            
    - **Again:**
      - **All the records inside a group are required to be same in a sense to your query, that is: choosing which record as reference doesn't matter.**
      - **If one group is not empty, and then will _HAVE ONE_ and must will _ONLY HAVE ONE_ record goes into the output, but which one depends on how SQL throws the dice'.**
      
    - [SQL vs MySQL: Rules about aggregate operations and GROUP BY](http://stackoverflow.com/questions/12843303/sql-vs-mysql-rules-about-aggregate-operations-and-group-by)

3. [How to understand buffer](Node.js/README.20160404.buffer.md)

4. [JavaScript variable scope](JavaScript/README.20160405.variable.scope.md)


