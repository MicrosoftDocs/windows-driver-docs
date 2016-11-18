---
title: Example Default Segmentation Filter
author: windows-driver-content
description: Example Default Segmentation Filter
MS-HAID:
- 'WIA\_tree\_316d3a51-b4ab-46d0-961a-51c3b5465189.xml'
- 'image.example\_\_default\_segmentation\_filter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 96c74ca6-0162-4991-b3f9-86c17c92ffc3
---

# Example: Default Segmentation Filter


A driver is not required to have its own segmentation filter in order to take advantage of the Microsoft segmentation filter, as long as it implements the WIA\_IPS\_SEGMENTATION property. Another possibility is for an IHV to provide its own segmentation filter, which during certain circumstances calls into the Microsoft default WIA segmentation filter. For example, an IHV might want to provide a very device-specific segmentation filter for multi-region detection during film scanning and use the segmentation filter provided by Microsoft during scans from the flatbed. To do this, an IHV WIA segmentation filter only needs to create *CLSID\_WiaDefaultSegFilter*, which implements *IWiaSegmentationFilter;* the segmentation filter would then call *DetectRegions*. The following code example shows how this can be done.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Example:%20Default%20Segmentation%20Filter%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


