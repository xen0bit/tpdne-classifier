for i in {1..1000}
do
   wget https://thispersondoesnotexist.com/image -O ./fake/"$i".jpg
done