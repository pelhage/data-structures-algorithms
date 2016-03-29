The program runs by going into the terminal, and typing `python solvemaze.py <mazename.txt>`

My program successfully solved for all mazes that were provided for the assignment, with the outputs printed below. Note that I modified some of the formatting for the maze to make it easier to read where the solved path was (denoted in periods).

Please note that most of the code I wrote to solve the maze is in the maze.py file!!!



MAZE 1 OUTPUT:
==========================================
EMPTY MAZE: maze1.txt
Start: (4, 1)
End: (3, 4)

%%%%%
% % %
%   %
% %  
% %%%
==========================================
Attempting to solve maze...
==========================================
STATUS: path found!
COMPLETED MAZE: maze1.txt

%%%%%
%-%-%
%...%
%.%..
%.%%%


MAZE 2 OUTPUT:
==========================================
EMPTY MAZE: maze2.txt
Start: (4, 1)
End: (3, 4)

%%%%%
% % %
% % %
% %  
% %%%
==========================================
Attempting to solve maze...
==========================================
STATUS: path not found
There was not a path found from the starting position the the end position, or, the maze is invalid




MAZE 3

==========================================
EMPTY MAZE: maze3.txt
Start: (17, 0)
End: (11, 18)

%%%%%%%%%%%%%%%%%%%
% %               %
% % %%% % %%%%%%%%%
%   %   %         %
% %%% %%%%%%%%% % %
% %   %       % % %
% %%%%% %%%%% %%% %
%   %       % %   %
%%% % %%%%% % % % %
%   % %   % % % % %
%%% % % % % % % % %
%   %   % % %   %  
% %%%%%%% %%%%%%% %
%       % %       %
%%%%% % % % %%%%% %
%   % % %   %   % %
% %%% % %%%%% % % %
      %       %   %
%%%%%%%%%%%%%%%%%%%
==========================================
Attempting to solve maze...
==========================================
STATUS: path found!
COMPLETED MAZE: maze3.txt

%%%%%%%%%%%%%%%%%%%
%-%---------------%
%-%-%%%-%-%%%%%%%%%
%---%---%---------%
%-%%%-%%%%%%%%%-%-%
%-%---%-------%-%-%
%-%%%%%-%%%%%-%%%-%
%---%-------%-%---%
%%%-%-%%%%%-%-%-%-%
%---%-%---%-%-%-%-%
%%%-%-%-%-%-%-%-%-%
%---%---%-%-%---%..
%-%%%%%%%-%%%%%%%.%
%----...%-%------.%
%%%%%.%.%-%-%%%%%.%
%---%.%.%---%...%.%
%-%%%.%.%%%%%.%.%.%
......%.......%...%
%%%%%%%%%%%%%%%%%%%