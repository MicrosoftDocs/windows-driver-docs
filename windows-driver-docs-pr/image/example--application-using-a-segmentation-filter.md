---
title: Example Application Using a Segmentation Filter
author: windows-driver-content
description: Example Application Using a Segmentation Filter
MS-HAID:
- 'WIA\_tree\_ff35540b-1bfe-4645-b3fe-2e9f05dcddba.xml'
- 'image.example\_\_application\_using\_a\_segmentation\_filter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3f7de6a2-5684-4c37-97bc-47f4727114ab
---

# Example: Application Using a Segmentation Filter


## <a href="" id="ddk-example-application-using-a-segmentation-filter-si"></a>


The following code example shows how a simple application could use the segmentation filter. For clarity, error-checking code has been omitted, as well as code to release and free interface pointers and memory.

```
IWiaSegmentationFilter *pWiaSegmentationFilter = NULL;
IWiaTransferCallback *pMyWiaTransferCallback = NULL;
IWiaTransfer  *pWiaTransfer = NULL;

...

pWiaItem2->QueryInterface(IID_IWiaTransfer, (void**)&pWiaTransfer);

pMyWiaTransferCallback = new MyWiaTransferCallback();


//
// Do preview scan.
//    
pWiaTransfer->Download(lFlags, pMyWiaTransferCallback);

//
// If an application changes any properties in pWiaItem2, it
// should call IWiaPropertyStorage::GetPropertyStream on
// that item to save its property settings (so they can be
// restored) before calling IWiaSegmentationFilter::DetectRegions.
//

if (ReadPropertyLong(WIA_IPS_SEGMENTATION_FILTER, &lUseSegFilter) &&
    (lUseSegFilter == WIA_USE_SEGMENTATION_FILTER)
{
    bstrSegmentation = SysAllocStr(WIA_SEGMENTATION_FILTER_STR);

    pWiaItem2->GetExtension(bstrSegmentation,
                            IID_IWiaSegmentationFilter,
                           (void**)& pWiaSegmentationFilter);

//
// m_pInputStream is a pointer to the IStream that the application&#39;s
// implementation of MyWiaTransferCallback::GetNextStream
// returns.
//
// Note: If the application has changed any properties into
// pWiaItem2 since the call to Download, it must now restore
// these properties with IWiaPropertyStorage::SetPropertyStream.
//

//
// The application is responsible for resetting m_pInputStream
// before calling DetectRegions!
//
    LARGE_INTEGER  ul = {0};

    m_pInputStream->Seek(ul, STREAM_SEEK_SET, NULL);

    pWiaSegmentationFilter->DetectRegions(m_pInputStream,
                                          pWiaItem2);

   ...
}

//
// Display the subregions to the users (if segmentation was
// supported) and let them pick the images they want to scan,
// as well as change the properties in the child items

//
// For each child item, pChildItem, do the following ( alternatively,
// do a folder acquisition on pWiaItem2).
//
IWiaTransfer  *pWiaTransferChild= NULL;

pChildItem->QueryInterface(IID_IWiaTransfer,
                           (void**)& pWiaTransferChild);

pWiaTransferChild->Download(lFlags, pMyWiaTransferCallback); 
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Example:%20Application%20Using%20a%20Segmentation%20Filter%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


