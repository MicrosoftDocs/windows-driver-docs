---
title: Example DownloadPreviewImage
description: Example DownloadPreviewImage
ms.assetid: 9b27492e-0725-4c8b-9101-3aaf5c9291d9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example: DownloadPreviewImage





The **DownloadPreviewImage** function downloads image data from the scanner by calling the preview component's **IWiaPreview::GetNewPreview** method. It then calls the **DetectSubregions** function if the application user wants to invoke the segmentation filter, which creates a child item under *pWiaItem2* for each region that it detects. For information about **DetectSubregions**, which is used in this example, see the [**IWiaSegmentationFilter::DetectRegions**](https://msdn.microsoft.com/library/windows/hardware/ff545030) method.

In this example, the application user sets the *m\_bUseSegmentationFilter* parameter by clicking a check box. If the application supports this, it should first check that the driver has a segmentation filter by calling **IWiaItem2::CheckExtension**. For information about **CheckImgFilter**, which is used in this example, see the **IWiaPreview::GetNewPreview** method in the Microsoft Windows SDK documentation.

```cpp
HRESULT
DownloadPreviewImage(
  IN IWiaItem2 *pWiaFlatbedItem2)
{
  HRESULT              hr = S_OK;
  BOOL                 bHasImgFilter  = FALSE;
  IWiaTransferCallback *pAppWiaTransferCallback = NULL;

  hr = CheckImgFilter(pWiaFlatbedItem2, &bHasImgFilter)

  if (SUCCEEDED(hr))
  {
     if (bHasImgFilter)
     {
        IWiaPreview *pWiaPreview = NULL;

        // In this example, the AppWiaTransferCallback class 
        // implements the IWiaTransferCallback interface.
         // The constructor of AppWiaTransferCallback sets the 
         // reference count to 1.
         pAppWiaTransferCallback = new AppWiaTransferCallback();

         hr = pAppWiaTransferCallback ? S_OK : E_OUTOFMEMORY;

         if (SUCCEEDED(hr))
         {
            // Acquire image from scanner
            hr = m_pWiaPreview->GetNewPreview(pWiaFlatbedItem2,
                                              0,
                                              pAppWiaTransferCallback);    
         }

         // m_FlatbedPreviewStream is the stream that
         // AppWiaTransferCallback::GetNextStream returned for the
         // flatbed item.
         // This stream is where the image data is stored after
         // the successful return of GetNewPreview.
         // The stream is passed into the segmentation filter
         // for region detection.
         if (SUCCEEDED(hr) && m_bUseSegmentationFilter)
         {
            DetectSubregions(m_FlatbedPreviewStream, pWiaFlatbedItem2);
         }

         if (pAppWiaTransferCallback)
         {
            // If the call to GetNewPreview was successful, the
            // preview component calls AddRef on the callback so
            // this call doesn't delete the object.

            pAppWiaTransferCallback->Release();
         }

      }
      else
      {
         // Do not create an instance of preview component if the 
         // driver does not come with an image-processing filter.
         // You can use a segmentation filter, however, if the driver
         // comes with one (omitted here).
      }
   }

   return hr;
}
```

 

 




