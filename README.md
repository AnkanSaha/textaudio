# text to audio file converter by python
I make a Python based text to audio file converter project. this project  is a open source project. You can download  this project.

To run this project , first run :-

    git clone https://github.com/AnkanSaha/textaudio.git

after downloading , run command :-

    cd textaudio

after run those command, run command :-

    pip install -r requirements.txt

after run those commands, run command :-

    python app.py

then a GUI has open.
 now follow the GUI instructions and convert a text massage into a audio file & save in your desktop.
 
 if you are make a new look of this package, just follow thease steps :
 
   just delete the 'app.py' file.
   
   make a new a 'xyz.py' in the same directory.
   
   then open the file and add thease line :-
   
    from main.texttoaudio import main
      
   Then add thease line of code in second line :-
   
    main()
