---
title: Example DetectSubregions
description: Example DetectSubregions
ms.date: 04/20/2017
---

# Example: DetectSubregions





The segmentation filter performs region detection on the stream (*pImageStream*) passed into the **DetectSubregions** method. For information on the **CreateSegmentationFilter** function, which is used in this example, see the **IWiaItem2::GetExtension** method in the Microsoft Windows SDK documentation.

```cpp
HRESULT
DetectSubregions(
   IN IStream   *pImageStream,
   IN IWiaItem2 *pWiaItem2)
{
   HRESULT                 hr                  = S_OK;
   IWiaSegmentationFilter* pSegmentationFilter = NULL;

   if (!pWiaItem2 || !pImageStream)
   {
      hr = E_INVALIDARG;
   }

   if (SUCCEEDED(hr))
   {
      hr = CreateSegmentationFilter(pWiaItem2, &pSegmentationFilter);
   }

   if (SUCCEEDED(hr))
   {
      hr = pSegmentationFilter->DetectRegions(pImageStream, pWiaItem2); 
   }

   if (pSegmentationFilter)
   {
      pSegmentationFilter->Release();
      pSegmentationFilter = NULL;
   }

   return hr;
}
```

 

 




