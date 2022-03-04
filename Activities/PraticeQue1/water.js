

function waterTrap(height)
    {
        
        let n = height.length;
        
        // Variable to store max water
        let res = 0;
 
        //traverse over array
        for(let i = 1; i < n - 1; i++)
        {
 
            // Find maximum element on its left
            let left = height[i];
            for(let j = 0; j < i; j++)
            {
                left = Math.max(left, height[j]);
            }
 
            // Find maximum element on its right
            let right = height[i];
            for(let j = i + 1; j < n; j++)
            {
                right = Math.max(right, height[j]);
            }
 
            // calculate and update maximum water value
            res += Math.min(left, right) - height[i];
        }
        return res;
    }
     
    let height = [4,2,0,3,2,5];
    
  
    var res = waterTrap(height);

    console.log(res);

    