---
title: Image Processing Code Example
description: Image Processing Code Example
ms.assetid: fe5ac3db-46e0-4162-9add-c3b0ae736926
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Image Processing Code Example





The following code example shows how to implement a simple image processing filter. This image processing filter supports brightness and contrast as well as the optional deskew and rotation properties.

**Note**   Portions of code are omitted from the following example for brevity.

 

```cpp
///
///  Constructor
///
CImageFilter::CImageFilter(VOID) :
    m_pWiaItem(NULL),
    m_pAppWiaTransferCallback(NULL),
    m_nRefCount(0),
    m_pCurrentStream(NULL)
{
    //
    // Nothing
    //
}

///
///  Destructor
///
CImageFilter::~CImageFilter()
{
    if (m_pWiaItem)
    {
        m_pWiaItem->Release();
        m_pWiaItem = NULL;
    }
    if (m_pAppWiaTransferCallback)
    {
        m_pAppWiaTransferCallback->Release();
        m_pAppWiaTransferCallback = NULL;
    }
}

//
// pWiaItem is the WIA item we are doing the download for.
// In the case of folder transfers, this will actually be
// the parent item of the images we are acquiring.
//
STDMETHODIMP
CImageFilter::InitializeFilter(
                  IN IWiaItem2  *pWiaItem,
                  IN IWiaTransferCallback  *pWiaTransferCallback)
{
    HRESULT  hr = S_OK;

    hr = (pWiaItem && pWiaTransferCallback) ? S_OK : E_INVALIDARG;

    //
    // InitializeFilter should only be called only once, but,
    // to be safe, we release any old resources we might still
    // reference before we take references to the new resources.
    //
    if (SUCCEEDED(hr))
    {
        if (m_pWiaItem)
        {
            m_pWiaItem->Release();
            m_pWiaItem = NULL;
        }
        if (m_pAppWiaTransferCallback)
        {
            m_pAppWiaTransferCallback->Release();
            m_pAppWiaTransferCallback = NULL;
        }

        m_pWiaItem = pWiaItem;
        m_pWiaItem->AddRef();
        m_pAppWiaTransferCallback = pWiaTransferCallback;
        m_pAppWiaTransferCallback->AddRef();
    }

    return hr;
}

STDMETHODIMP
CImageFilter::FilterPreviewImage(
                  IN IWiaItem2  *pWiaChildItem,
                  IN RECT  InputImageExtents,
                  IN IStream  *pInputStream)
{
    IStream  *pAppStream   = NULL;
    BSTR  bstrItemName     = NULL;
    BSTR  bstrFullItemName = NULL;
    LONG  xpos = 0, ypos = 0, width = 0, height = 0;
    LONG  lBrightness = 0;
    LONG  lContrast   = 0;
    LONG  lDeskewX    = 0;
    LONG  lDeskewY    = 0;
    LONG  lRotation   = PORTRAIT;

    HRESULT  hr;

    hr = m_pAppWiaTransferCallback ? S_OK : E_UNEXPECTED;

    //
    // Read all of the properties we need.
    //
    if (SUCCEEDED(hr))
    {
        hr = ReadAllProperties(pWiaChildItem,
                               &xpos,
                               &ypos,
                               &width,
                               &height,
                               &bstrItemName,
                               &bstrFullItemName,
                               &lBrightness,
                               &lContrast,
                               &lRotation,
                               &lDeskewX,
                               &lDeskewY);
    }

    //
    // If the upper left corner of the passed image does
    // not correspond to (0,0) on the flatbed, adjust
    // xpos and ypos accordingly in order to "cut out"
    // the correct region represented by pWiaChildItem
    // from pInputStream.
    //
    if (SUCCEEDED(hr))
    {
        xpos = xpos - InputImageExtents.left;
        ypos = ypos - InputImageExtents.top;
    }

    //
    // Now get the application stream and write to it.
    //
    if (SUCCEEDED(hr))
    {
        hr = m_pAppWiaTransferCallback->GetNextStream(
                                            0,
                                            bstrItemName,
                                            bstrFullItemName,
                                            &pAppStream);
    }
    if (SUCCEEDED(hr))
    {
        //
        // DoFiltering is where the actual filtering is done.
        // This function is left out to simplify this example.
        // DoFiltering reads the unfiltered image data from
        // pInputStream and writes the filtered (and possibly
        // deskewed) image into pAppStream.
        //
        // Note: A "real" implementation of DoFiltering should send
        // WIA_TRANSFER_MSG_STATUS messages to the application's
        // callback interface, m_pAppWiaTransferCallback.
        // DoFiltering should preferably also be able to
        // work on bands of data in the case where there is no
        // rotation or deskewing being performed.
        //
        hr = DoFiltering(lBrightness,
                         lContrast,
                         lDeskewX,
                         lDeskewY,
                         pInputStream,
                         pAppStream,
                         xpos,
                         ypos,
                         width,
                         height,
                         lRotation);
    }

    if (pAppStream)
    {
        pAppStream->Release();
    }

    return hr;
}

//
// Our simple image processing filter implementation always
// caches all data internally, and it does not write data back
// to the application's stream until it receives
// WIA_TRANSFER_MSG_END_OF_STREAM. A "real" image-processing
// filter should be able to work on bands of data -- at least
// if there is no rotation or deskew set into the item.
//
// In order to find out how many bytes have been written
// into the application's stream, we store an interface
// pointer to the current filtering stream, m_pCurrentStream.
// When we reach the end of the stream, we must notify the
// filtering stream that it should filter and write all of
// its image data to the application stream, if it has not
// already done so.
//
STDMETHODIMP
CImageFilter::TransferCallback(
                  IN LONG  lFlags,
                  IN WiaTransferParams  *pWiaTransferParams)
{
    HRESULT  hr;

    hr = m_pAppWiaTransferCallback ? S_OK : E_UNEXPECTED;

    if (SUCCEEDED(hr))
    {
        //
        // Note: The percent reflects the amount of scanning
        // the driver reports, whereas the "BytesWritten" member
        // is the actual number of bytes that we have written
        // to the application's stream.
        // We do not modify the percent, however we have to
        // modify the ulBytesWrittenToCurrentStream member.
        //
        if ((pWiaTransferParams->lMessage ==
                            WIA_TRANSFER_MSG_END_OF_STREAM) &&
             m_pCurrentStream )
        {
            hr = m_pCurrentStream->Flush();
        }
        else if (m_pCurrentStream)
        {
            pWiaTransferParams->ulBytesWrittenToCurrentStream =
                                  m_pCurrentStream->m_cBytesWritten;
        }

        hr = m_pAppWiaTransferCallback->TransferCallback(
                                            lFlags,
                                            pWiaTransferParams);
        if (m_pCurrentStream &&
            (pWiaTransferParams->lMessage ==
                            WIA_TRANSFER_MSG_END_OF_STREAM))
        {
            m_pCurrentStream->Release();
            m_pCurrentStream = NULL;
        }
    }
    return hr;
}

//
// GetNextStream creates a filtering stream whose Write method
// writes to the application's stream. Because the item
// represented by bstrFullItemName might be a child item of
// the item passed into InitializeFilter, we have to call
// FindItemByName to retrieve the actual item.
//
STDMETHODIMP
CImageFilter::GetNextStream(
                  IN  LONG     lFlags,
                  IN  BSTR     bstrItemName,
                  IN  BSTR     bstrFullItemName,
                  OUT IStream  **ppDestination)
{
    HRESULT    hr;
    IStream    *pAppStream      = NULL;
    IStream    *pCachingStream  = NULL;
    IWiaItem2  *pCurrentWiaItem = NULL;
    LONG       lBrightness      = 0;
    LONG       lContrast        = 0;
    LONG       lDeskewX         = 0;
    LONG       lDeskewY         = 0;
    LONG       lRotation        = PORTRAIT;

    hr = m_pAppWiaTransferCallback ? S_OK : E_UNEXPECTED;

    if (m_pCurrentStream)
    {
        m_pCurrentStream->Release();
        m_pCurrentStream = NULL;
    }
    if (SUCCEEDED(hr))
    {
        hr = m_pAppWiaTransferCallback->GetNextStream(
                                            lFlags,
                                            bstrItemName,
                                            bstrFullItemName,
                                            &pAppStream);
    }
    if (SUCCEEDED(hr))
    {
        hr = m_pWiaItem->FindItemByName(
                             0,
                             bstrFullItemName,
                             &pCurrentWiaItem);
    }
    //
    // Here we read all properties from pCurrentWiaItem
    // that we need in order to do the filtering.
    // Note: We do not need to read all the properties
    // like we did in update preview. The driver should
    // always return the area represented by the bounding
    // rectangle, so no "cutting" will be done in this case.
    //
    if (SUCCEEDED(hr))
    {
        hr = ReadDownloadProperties(pCurrentWiaItem,
                                    &lBrightness,
                                    &lContrast,
                                    &lRotation,
                                    &lDeskewX,
                                    &lDeskewY);
    }

    if (SUCCEEDED(hr))
    {
        hr = CreateStreamOnHGlobal(0, TRUE, &pCachingStream);
        if (SUCCEEDED(hr))
        {
            //
            // The implementation of CalculateAndSetSize is
            // omitted here. CalculateAndSetSize estimates the
            // maximum size of the image we are about to download;
            // then it calls SetSize on the caching stream.
            // This size calculation is for performance reasons
            // (if the image we are downloading is very large).
            // A "real" image processing filter should probably
            // use a higher-performance stream implementation.
            //
            CalculateAndSetSize(pCurrentWiaItem, pCachingStream);
        }
    }
    if (SUCCEEDED(hr))
    {
        m_pCurrentStream = new CMyFilterStream(
                                   pAppStream,
                                   pCachingStream,
                                   lBrightness,
                                   lContrast,
                                   lRotation,
                                   lDeskewX,
                                   lDeskewY);
        if (m_pCurrentStream)
        {
            hr = m_pCurrentStream->QueryInterface(
                                       IID_IStream,
                                       (void**)ppDestination);
        }
        else
        {
            hr = E_OUTOFMEMORY;
        }
    }
    if (pAppStream)
    {
        pAppStream->Release();
    }
    if (pCachingStream)
    {
        pCachingStream->Release();
    }
    if (pCurrentWiaItem)
    {
        pCurrentWiaItem->Release();
    }

    return hr;
}

//
// FILTERING STREAM IMPLEMENTATION
//

///
/// Constructor - Note: Sets reference count to 1.
///
CMyFilterStream::CMyFilterStream(
                     IStream  *pAppStream,
                     IStream  *pCachingStream,
                     LONG  lBrightness,
                     LONG  lContrast,
                     LONG  lRotation,
                     LONG  lDeskewX,
                     LONG  lDeskewY) :

    m_pAppStream(pAppStream),
    m_pCachingStream(pCachingStream),
    m_nRefCount(1),
    m_cBytesWritten(0),
    m_lBrightness(lBrightness),
    m_lContrast(lContrast),
    m_lRotation(lRotation),
    m_lDeskewX(lDeskewX),
    m_lDeskewY(lDeskewY)
{
    if (m_pAppStream)
    {
        m_pAppStream->AddRef();
    }
    if (m_pCachingStream)
    {
        m_pCachingStream->AddRef();
    }
}

///
/// Destructor
///
CMyFilterStream::~CMyFilterStream()
{
    if (m_pAppStream)
    {
        m_pAppStream->Release();
    }
    if (m_pCachingStream)
    {
        m_pCachingStream->Release();
    }
}

//
// The only IStream method of interest here is Write.
// For this simple ImageProcesing filter, we always write the
// data into the "caching stream". The filtered image data is
// not written into the application's stream until we receive
// an end-of-stream message.
//
STDMETHODIMP
CMyFilterStream::Write(const void *pv, ULONG cb, ULONG *pcbWritten)
{
    return m_pCachingStream->Write(pv, cb, pcbWritten);
}

//
// Flush is called when our callback routine receives
// WIA_TRANSFER_MSG_END_OF_STREAM. In this simple implementation,
// this is when we first write the data to the application's
// stream, m_pAppStream.
//
HRESULT
CMyFilterStream::Flush(VOID)
{
    HRESULT hr;

    hr = DoFiltering(m_pAppWiaTransferCallback,
                     m_lBrightness,
                     m_lContrast,
                     m_lRotation,
                     m_lDeskewX,
                     m_lDeskewY,
                     m_pCachingStream,
                     m_pAppStream);

    if (m_pAppStream)
    {
        m_pAppStream->Release();
        m_pAppStream = NULL;
    }
    if (m_pCachingStream)
    {
        m_pCachingStream->Release();
        m_pCachingStream = NULL;
    }

    return hr;
}
```

 

 




