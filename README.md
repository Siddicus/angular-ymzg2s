<h6> angular-ymzg2s</h6>
<h1>The Game-Not So Greedy Anymore! </h1>
[Edit on StackBlitz ⚡️](https://stackblitz.com/edit/angular-ymzg2s)


## Outline
In this semi-local approach depicted above, a little description first of the purposes of each of these major functions:

- **Post_Short**: Uses the manhattan distance ignoring the presence of obstacles at first and later extracts single sub-path from the lists of available endpoints. If no such path is found( The list of available choice is null), it calls the *good_point_changer* function to choose the non-local starting point assuming the grid is topologically simply-connected.
- **ver_bool_response**: Checks if the optimum movement could be made towards the target and returns a bool response if it's not possible.
- **bool_cord_response**: Looks for the optimum alternative starting point incase Post_Short encounters an *obstacle*. Incase, no such alternative could be found, it calls *good_point_generator*. 
- **destination**: Returns a bool response if the destination is reached. It has to be checked at multiple end-points.
- **Good_point_generator**: As mentioned in the description of *Post_Short*, it is called when it becomes impossible to proceed along with optimum path. It generates the simply-connected point and further calls the *Post_Short* with a new start_point
- **Path Post Processing**: It comprises of 3 sub-functions, namely  
  - **extra_branch_cut**: It prunes the path incase the object has to return back and follow the other expected trajectory in continuity( *It is possible in this algorithm, that the consecutive point of the path are non-local (Only incase when Good_point_generator is called). But, this is easily fixed and turns out to be a boon!*
  - **path_processing**: It process the path incase when there is a disconnected branch in the path.
  - **list_completion**: It completes the path incase there are any jumps (the manhattan distance between successive points>1) in the final path

<img src="https://raw.githubusercontent.com/Siddicus/angular-ymzg2s/master/outline.JPG" width="700" height="620">

## Explaination Of Flow Chart

-At first the Post_Short is called. It extracts the most optimal sub-path from the available list. Incase it encounters an obstacle-> 
  - If it is able to continue from the same point(i.e, ver_bool_response is True), Post_Short is called back with the same endpoint that the Post_Short in the previous stage terminated at. If the response if False, bool_cord_response is called.
- In case bool_cord_response is able to find the optimal change in the route and if the destination is not reached after implementing that, Post_Short is called again with the new start point that is provided by the bool_cord_response. Incase, it is unable to find any alternative starting points for the Post_Short, Good_point_generator is called and it then provides the Post_short with the newly generated possibly non-local point.

The above process is repeated untill the destination is reached, and later the path_post_processing is done. 

## An Example

<img src="https://raw.githubusercontent.com/Siddicus/angular-ymzg2s/master/breakpoints.JPG" width="680" height="500">
- Post_Short generates two possible paths and out of them, the endpoint(3,1) of the first is chosen.
- Since, it can no longer proceed in the desired target, ver_bool_response is called and it is False, and bool_cord_response is called that gives us the point (3,1) --> (1,1).
- Post_Short is called to start from (1,1) and it chooses to end at (3,1) -> ver_bool_response is called it is False again, and bool_cord_response is called giving us the point (2,3) and calling Post_Short again with (2,3) as its start point
- From here is directly reaches its destination and the loop ends.

