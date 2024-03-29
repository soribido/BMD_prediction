# BMD prediction
Bone mineral density (BMD) prediction in CT images based on deep residual CNN + XAI Interpretation

**Paper**   
[Kang, J. W., Park, C., Lee, D. E., Yoo, J. H., & Kim, M. (2023). Prediction of bone mineral density in CT using deep learning with explainability. Frontiers in Physiology, 13, 2735.](https://www.frontiersin.org/articles/10.3389/fphys.2022.1061911/full)

## Workflow
![workflow](/readme-figure/workflow.png)
  
## L1 Segmentation
In order to investigate which area had a great impact on the prediction of BMD, we divided the experiment into three cases.  
* ``Case 1 : Cropped images``  
* ``Case 2 : Entire-vertebrae-masked images``  
* ``Case 3 : Vertebral-body-masked images``  
  
U-Net-based model was applied to segment the L1 region.  
![segmentation](/readme-figure/segmentation.png)  

## BMD Prediction
Deep resiudal CNN for BMD estimation.  

We achieved a maximum correlation coefficient of 0.905 for the test set.  
  
* **Estimation Network**  

![prediction](/readme-figure/prediction.png)
  
  

* **Estimation Result**  

<!-- ![pred_result](/readme-figure/prediction_result.png){: width="50%",height="50%"} -->
<p align="center">
    <img src="./readme-figure/prediction_result.png", width="65%",height="65%">
</p>


## XAI Interpretation
Grad-CAM is well-known XAI technique used to investigate the attention of a DL network toward an image.  
  
We modified Grad-CAM for this study because it is specialized in a classifer, whereas our network is an estimator (regressor).  
  
Grad-RAM converted the ReLU operator in Grad-CAM to an absolute operator because it considered the features that have a significant impact on the estimate, regardless of the direction (sign) of the gradient.
   
$$L_{Grad-RAM}\left(i,j\right)=\left|\sum_{k}{\alpha_kA_k\left(i,j\right)}\right|,\ \ \ \ \alpha_k=\frac{1}{Z}\sum_{i}\sum_{j}\frac{\partial y}{\partial A_k(i,j)}$$
  
Grad-RAMP multiplied each gradient with respect to every pixel $(i,j)$ with the corresponding pixels to consider pixel attribution.  
    
$$L_{Grad-RAMP}\left(i,j\right)=\left|\sum_{k}{g_k\odot A_k\left(i,j\right)}\right|,\ \ \ \ g_k=\frac{\partial y}{\partial A_k(i,j)}$$
  
* $k$ : Channel index of the convolutional layer  
* $\alpha_{k}(i,j)$ : $k$ th weight  
* *Z* : The number of pixels in the feature map  
* $A_{k}(i,j)$ : Feature map of the last convolutional layer  
* $\odot$ : Hadamard product operator 
  
  
* **XAI result**  
<!-- ![xai](/readme-figure/xai.png) -->
<p align="center">
    <img src="./readme-figure/xai.png", width="80%",height="80%">
</p>    
 
