for i in {1..70000}
do
   echo "wget https://thispersondoesnotexist.com/image -O ./fake/"$i".jpg" >> list.txt
done
