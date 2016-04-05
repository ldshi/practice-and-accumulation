- JavaScript variable scope
  - **No such thing as block scope in JavaScript (ES5; ES6 introduces let)**
  - [JavaScript variable scope](http://stackoverflow.com/questions/500431/what-is-the-scope-of-variables-in-javascript)
  ```
  findBestCombination = (base, accumulator, round, targetValue, bestCombination) ->
    if round <= base.length
      if round == 0
        accumulator = base.reduce(((o, v, i) ->
          tempKey = v.toFixed(2)
          if !o[tempKey]
            o[tempKey] = [i]
          return o
        ), {})
      else
        for key of accumulator
          if round == base.length
            if parseFloat(key) <= parseFloat(targetValue) and parseFloat(key) > bestCombination.bestValue
              bestCombination.bestValue = parseFloat(key)
              bestCombination.indexes = accumulator[key]

          if accumulator[key].length == round
            i = 0
            while i < base.length
              if accumulator[key].indexOf(i) == -1
                tempKey = (parseFloat(key) + parseFloat(base[i])).toFixed(2)
                if !accumulator[tempKey]
                  accumulator[tempKey] = accumulator[key].concat([i])
              i++

      findBestCombination base, accumulator, ++round, targetValue, bestCombination
  ```


