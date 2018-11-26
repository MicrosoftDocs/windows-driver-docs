---
title: Example Default Segmentation Filter
description: Example Default Segmentation Filter
ms.assetid: 96c74ca6-0162-4991-b3f9-86c17c92ffc3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example: Default Segmentation Filter


A driver is not required to have its own segmentation filter in order to take advantage of the Microsoft segmentation filter, as long as it implements the WIA\_IPS\_SEGMENTATION property. Another possibility is for an IHV to provide its own segmentation filter, which during certain circumstances calls into the Microsoft default WIA segmentation filter. For example, an IHV might want to provide a very device-specific segmentation filter for multi-region detection during film scanning and use the segmentation filter provided by Microsoft during scans from the flatbed. To do this, an IHV WIA segmentation filter only needs to create *CLSID\_WiaDefaultSegFilter*, which implements *IWiaSegmentationFilter;* the segmentation filter would then call *DetectRegions*. The following code example shows how this can be done.

```cpp
STDMETHODIMP
SegFilter::DetectRegions(
   IN LONG       lFlags,
     IN IStream    *pInputStream,
     IN IWiaItem2  *pWiaItem2)
{
    HRESULT  hr                = S_OK;
    GUID     categoryGUID      = {0};
    BOOL     bUseDefaultFilter = FALSE;

    ...


    if (SUCCEEDED(hr))

    {
        ReadPropertyLong(pWiaItem2,
                         WIA_IPA_ITEM_CATEGORY,
                         &categoryGUID);
 
        if (categoryGUID == WIA_CATEGORY_FILM)
        {
            bUseDefaultFilter = FALSE;
        }
        else if (categoryGUID == WIA_CATEGORY_FLATBED)
        {
            bUseDefaultFilter = TRUE;
        }
        else
        {
            //
            // This scanner only comes with flatbed and film items.
            //
            hr = E_INVALIDARG;
        }
    }
 
    ...
 
    if (SUCCEEDED(hr) && bUseDefaultFilter)
    {
        //
        // This must be on the flatbed item - use the Microsoft Default WIA Segmentation Filter.
        //

        IWiaSegmentationFilter *pDefaultSegFilter = NULL;
 
        hr = CoCreateInstance(CLSID_WiaDefaultSegFilter,
                              NULL,
                              CLSCTX_INPROC_SERVER,
                              IID_IWiaSegmentationFilter,
                              reinterpret_cast<void **>(&pDefaultSegFilter));
        if (SUCCEEDED(hr))
        {
            hr = pDefaultSegFilter->DetectRegions(lFlags, pInputStream, pWiaItem2);
        }
 
        if (pDefaultSegFilter)
        {
            pDefaultSegFilter->Release();
            pDefaultSegFilter = NULL;
        }
    }
    else if (SUCCEEDED(hr))
    {
        //
        // This is on the film item - use the default WIA segmentation algorithm.
        //
        ...
    }
    ...
}
```

 

 




