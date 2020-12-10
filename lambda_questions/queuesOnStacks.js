function queueOnStacks(requests) {
    var left = [];
    var right = [];
  
    function insert(x) {
      left.push(x)
    }
  
    function remove() {
      if (left.length == 0 && right.length == 0) {
          return right
      }
      
      if (right.length == 0) {
          while (left.length != 0) {
              right.push(left.pop())
          }
      }
      return right.pop()
    }
  
    ans = [];
    for (var i = 0; i < requests.length; i++) {
      var req = requests[i].split(" ");
      if (req[0] === "push") {
        insert(parseInt(req[1]));
      } else {
        ans.push(remove());
      }
    }
    return ans;
  }