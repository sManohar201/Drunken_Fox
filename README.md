# Drunken_Fox
EE5900_Intro_to_Robotics

GitHub commands: </br>

git commit --amend </br>
This can be used in two scenarios: </br>
1) if you want to edit the last commit message. </br>
2) see the following example: </br>
$ git commit -m 'first commit' </br>
$ git add missed_file </br>
$ git commit --amend  </br>
This will add "missed_file" to the 'first commit'

Things to note: </br>

(Do not push your local commits to the remote repository unless you are sure that no further changes will be made. 
If you pushed the local files to the remote folder, do not try to edit the remote repository commits. It will cause a lot of trouble.)  </br>

Build the package, in the main directory before you run the simulation. </br>

To run the simulation, </br>
`roslaunch jackal_sim lab_two.launch` </br>

A tutorial page has been added to the wiki for any reference. 


