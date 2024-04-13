---
title: Add Image Format Support
description: Add Image Format Support
ms.date: 03/27/2023
---

# Add Image Format Support

A WIA minidriver reports image formats to the WIA service in the [**IWiaMiniDrv::drvGetWiaFormatInfo**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo) method.

## Implement IWiaMiniDrv::drvGetWiaFormatInfo

The WIA service calls the **IWiaMiniDrv::drvGetWiaFormatInfo** method to obtain the WIA device-supported TYMED and FORMAT pairs.

The WIA driver should allocate memory (to be stored in this WIA driver and freed by this WIA driver) to contain an array of WIA_FORMAT_INFO structures (described in the Microsoft Windows SDK documentation). A pointer to the WIA driver-allocated memory should be passed to *ppwfi*. This isn't done directly, but with a pointer to a pointer. In the following example, *ppwfi* is set with the address of m_WIAFormatInfo\[0\], which in turn evaluates to the address of the first member of the structure.

It's important to note that the WIA service won't free this memory. It's the responsibility of the WIA driver to manage this allocated memory.

The WIA driver should write the number of structures that are allocated in the memory location to which the *pcelt* parameter points.

The WIA device should set the **guidFormatID** member of the WIA_FORMAT_INFO structure to the image format GUID. The device should set the **lTymed** member of this structure to the TYMED value associated with the image format GUID:

Valid TYMED values (also known as "Media Type") are:

TYMED_FILE

TYMED_MULTIPAGE_FILE

TYMED_CALLBACK

TYMED_MULTIPAGE_CALLBACK

The following example shows an implementation of [**IWiaMiniDrv::drvGetWiaFormatInfo**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo):

```cpp
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
