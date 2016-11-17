---
title: Example Simple Segmentation Filter
author: windows-driver-content
description: Example Simple Segmentation Filter
MS-HAID:
- 'WIA\_tree\_a5bd9bd7-cd4a-437e-8cac-5655b7420fe7.xml'
- 'image.example\_\_simple\_segmentation\_filter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9c77fea4-61d9-4bec-8d8d-35436d00c1ed
---

# Example: Simple Segmentation Filter


## <a href="" id="ddk-example-simple-segmentation-filter-si"></a>


The following code example shows how a simple segmentation filter can be implemented. The segmentation filter in the example does not use the [**WIA\_IPS\_DESKEW\_X**](https://msdn.microsoft.com/library/windows/hardware/ff552581) and [**WIA\_IPS\_DESKEW\_Y**](https://msdn.microsoft.com/library/windows/hardware/ff552587) properties. For clarity, error checking code has been omitted.

```
typedef struct _SUB_RECT
{
    LONG  xpos;
    LONG  ypos;
    LONG  width;
    LONG  height;
} SUB_RECT;

STDMETHODIMP
SegFilter::DetectRegions(IN IStream  *pInputStream,
                         IN IWiaItem2  *pWiaItem2)
{
    HRESULT   hr = S_OK;
    SUB_RECT  pSubRegions = NULL;
    ULONG     cRegionsFound = 0;
    LONG      parent_xpos, parent_ypos;
    GUID      formatGUID = {0};

    LONG  lItemFlags = WiaItemTypeGenerated |
                       WiaItemTypeTransfer |
                       WiaItemTypeImage |
                       WiaItemTypeFile |
                       WiaItemTypeProgrammableDataSource;

    LONG  lCreationFlags = COPY_PARENTS_PROPERTY_VALUES;

    ReadPropertyGUID(pWiaItem2, WIA_IPA_FORMAT, &formatGUID);

    //
    // The algorithm that performs the actual region
    // detection has been omitted for clarity.
    //
    FindSubRegions(pInputStream,
                   formatGUID,
                   &pSubRegions,
                   &cRegionsFound);

    ReadPropertyLong(pWiaItem2, WIA_IPS_XPOS, &parent_xpos);
    ReadPropertyLong(pWiaItem2, WIA_IPS_YPOS, &parent_ypos);

    //
    // For each subimage that was found, create
    // a child item under pWiaItem2 into which
    // the coordinates for the subimage are set.
    //
    for (int i = 0; i < cRegionsFound; i++)
    {
        BSTR       bstrChildName = NULL;
        BSTR       bstrFullChildName = NULL;
        IWiaItem2  *pChildIWiaItem = NULL;

        GetNamesForChild(i,
                         &bstrChildName,
                         &bstrFullChildName);

        pWiaItem2->CreateChildItem(lItemFlags,
                                   lCreationFlags,
                                   bstrChildName,
                                   &pChildIWiaItem);

        WritePropertyLong(pChildWiaItem,
                          WIA_IPS_XPOS,
                          parent_xpos + pSubRegions[i].xpos);

        WritePropertyLong(pChildWiaItem,
                          WIA_IPS_YPOS,
                          parent_ypos + pSubRegions[i].ypos);

        WritePropertyLong(pChildWiaItem,
                          WIA_IPS_XEXTENT,
                          pSubRegions[i].width);

        WritePropertyLong(pChildWiaItem,
                          WIA_IPS_YEXTENT,
                          pSubRegions[i].height);

        pChildIWiaItem->Release();
        SysFreeString(bstrChildName);
        SysFreeString(bstrFullChildName);
    }

    if (pSubRegions)
    {
        free(pSubRegions);
    }

    return hr;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Example:%20Simple%20Segmentation%20Filter%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


