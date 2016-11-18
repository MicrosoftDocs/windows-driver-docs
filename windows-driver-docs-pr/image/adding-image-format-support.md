---
title: Adding Image Format Support
author: windows-driver-content
description: Adding Image Format Support
MS-HAID:
- 'WIA\_drv\_basic\_cc1855e3-5119-44d9-9824-a9afd8cfd10c.xml'
- 'image.adding\_image\_format\_support'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ffa7c0d-23ec-402a-a0b5-fb5596a851bf
---

# Adding Image Format Support


## <a href="" id="ddk-adding-image-format-support-si"></a>


A WIA minidriver reports image formats to the WIA service in the [**IWiaMiniDrv::drvGetWiaFormatInfo**](https://msdn.microsoft.com/library/windows/hardware/ff543986) method.

### <a href="" id="implementing-iwiaminidrv-drvgetwiaformatinfo"></a>Implementing IWiaMiniDrv::drvGetWiaFormatInfo

The WIA service calls the **IWiaMiniDrv::drvGetWiaFormatInfo** method to obtain the WIA device-supported TYMED and FORMAT pairs.

The WIA driver should allocate memory (to be stored in this WIA driver and freed by this WIA driver) to contain an array of WIA\_FORMAT\_INFO structures (described in the Microsoft Windows SDK documentation). A pointer to the WIA driver-allocated memory should be passed to *ppwfi*. This is not done directly, but with a pointer to a pointer. In the following example, *ppwfi* is set with the address of m\_WIAFormatInfo\[0\], which in turn evaluates to the address of the first member of the structure.

It is important to note that the WIA service will not free this memory. It is the responsibility of the WIA driver to manage this allocated memory.

The WIA driver should write the number of structures that are allocated in the memory location to which the *pcelt* parameter points.

The WIA device should set the **guidFormatID** member of the WIA\_FORMAT\_INFO structure to the image format GUID. The device should set the **lTymed** member of this structure to the TYMED value associated with the image format GUID:

Valid TYMED values (also known as "Media Type") are:

TYMED\_FILE

TYMED\_MULTIPAGE\_FILE

TYMED\_CALLBACK

TYMED\_MULTIPAGE\_CALLBACK

The following example shows an implementation of [**IWiaMiniDrv::drvGetWiaFormatInfo**](https://msdn.microsoft.com/library/windows/hardware/ff543986):

```
HRESULT _stdcall CWIADevice::drvGetWiaFormatInfo(
  BYTE            *pWiasContext,
  LONG            lFlags,
  LONG            *pcelt,
  WIA_FORMAT_INFO **ppwfi,
  LONG            *plDevErrVal)
{
    //
    // If the caller did not pass in the correct parameters,
    // then fail the call with E_INVALIDARG.
    //

    if ((!pWiasContext)||(!plDevErrVal)||(!pcelt)||(!ppwfi)) {
        return E_INVALIDARG;
    }

    //
    // check if WIA_FORMAT_INFO array has been initialized.
    //
    // NOTE: m_WIAFormatInfo is a member variable that has been
    //       defined as    WIA_FORMAT_INFO m_WIAFormatInfo[2];
    //
    //

    if (m_WIAFormatInfo[0].lTymed == TYMED_NULL) {

        //
        // add all supported formats and corresponding TYMED values
        // here
        //

        m_WIAFormatInfo[0].guidFormatID = WiaImgFmt_MEMORYBMP;
        m_WIAFormatInfo[0].lTymed       = TYMED_CALLBACK;

        m_WIAFormatInfo[1].guidFormatID = WiaImgFmt_BMP;
        m_WIAFormatInfo[1].lTymed       = TYMED_FILE;
    }

    *plDevErrVal = 0;
    *ppwfi = &m_WIAFormatInfo[0];
    *pcelt = 2; // number of formats in returned array

    return S_OK;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Adding%20Image%20Format%20Support%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


