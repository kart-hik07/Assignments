img1=imread('C:\Users\kart0\OneDrive\Desktop\HW.png');
size(img1)
imshow(img1);



rc=img1(:,:,1);
imshow(rc);
gc=img1(:,:,2);
imshow(gc);
bc=img1(:,:,3);
imshow(bc);


img2=rgb2gray(img1);
imshow(img2);


Level=graythresh(img2)



img3=im2bw(img2,Level);
imshow(img3);


e=edge(img3);
array=[];
for i = 1:1:265
    for j = 1:1:661
        if(e(i,j)==1)
            array2=[i,j];
            array=vertcat(array, array2);
        end
    end
end
imshow(e);
hold on
s=size(array);
for i = 1:1:s(1)
    plot(array(i,2), array(i,2), '*g', 'linewidth', 5);
    pause(0.1);
end

