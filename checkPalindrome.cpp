bool checkPalindrome(char str[]){


  /* Don't write main().
   *  Don't read input, it is passed as function argument.
   *  Return output and don't print it.
   *  Taking input and printing output is handled automatically.
   */
    int length = 0;
    for(int i=0; str[i] != '\0'; i++){
        length++;
    }
    
    //bool palindrome = true;
    for(int i=0; i<length/2; i++){
        if(str[i] != str[length-i-1]){
            //palindrome = false;
            //break;
            return false;
        }
    }
  
    return true;
}
