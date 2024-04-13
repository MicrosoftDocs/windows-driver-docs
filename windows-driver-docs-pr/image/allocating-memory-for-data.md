---
title: Allocating Memory for Data
description: Allocating Memory for Data
ms.date: 03/27/2023
---

# Allocating Memory for Data

The WIA service relies on the information supplied in the [**MINIDRV_TRANSFER_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_minidrv_transfer_context) structure to perform a proper data transfer. 

The members of this structure that are relevant to the WIA minidriver are:

**bClassDrvAllocBuf** − WIA service allocation Boolean.

**pTransferBuffer** − Pointer to memory allocated for the transferred data.

**lBufferSize** − Size of the memory pointed to by the **pTransferBuffer** member.

If the **bClassDrvAllocBuf** member of the MINIDRV_TRANSFER_CONTEXT structure is set to **TRUE**, then the WIA service allocated memory for the minidriver. If the **bClassDrvAllocBuf** member is set to **FALSE**, the WIA service did not allocate any memory for the minidriver.

The minidriver should allocate memory using the **CoTaskMemAlloc** function (described in the Microsoft Windows SDK documentation). The minidriver should then store the pointer to the memory location in **pTransferBuffer** and the size of the memory in **lBufferSize** (in bytes).

The **bClassDrvAllocBuff** member is set to **FALSE** only if the [**WIA_IPA_TYMED**](./wia-ipa-tymed.md) property is set to TYMED_FILE or TYMED_MULTIPAGE_FILE, and the [**WIA_IPA_ITEM_SIZE**](./wia-ipa-item-size.md) property is set to zero.

The minidriver must be careful not to overfill the buffer pointed to by the **pTransferBuffer** member. You can avoid this by writing data in amounts less than or equal to the value stored in the **lBufferSize** member.

## Enhancing Data Transfer Performance by Using Minimum Buffer Size

The WIA minidriver can control the amount of memory used during the data transfer by setting the [**WIA_IPA_ITEM_SIZE**](./wia-ipa-item-size.md) and [**WIA_IPA_BUFFER_SIZE**](./wia-ipa-buffer-size.md) properties.

A WIA application uses the WIA_IPA_BUFFER_SIZE property to determine the minimum transfer buffer size to request during a memory transfer. The larger this value is, the larger the requested band size will be. If a WIA application requests a buffer that is smaller in size than the value in the WIA_IPA_BUFFER_SIZE property, the WIA service ignores this requested size and asks the WIA minidriver for a buffer that is WIA_IPA_BUFFER_SIZE bytes in size. The WIA service always asks the WIA minidriver for buffers that are at least WIA_IPA_BUFFER_SIZE bytes in size.

The value that the WIA_IPA_BUFFER_SIZE property contains is the minimum amount of data an application can request at any given time. The larger the buffer size, the larger the requests will be to the device. Buffer sizes that are too small can slow performance of the data transfer.

It is recommended that you set the WIA_IPA_BUFFER_SIZE property to a reasonable size to allow the device to transfer data at an efficient rate. Do this by balancing the number of requests (buffer size not too small) and the number of time-consuming requests (buffer too large) for your device in order to ensure optimal performance.

You should set the [**WIA_IPA_ITEM_SIZE**](./wia-ipa-item-size.md) property to zero if the WIA minidriver can transfer data. If the transfer type is TYMED_FILE or TYMED_MULTIPAGE_FILE, it is the minidriver's responsibility to allocate memory for the data buffer to be passed to the WIA service function that writes to the file. This provides consistency in the implementation of the [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method.

The [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) method is called by the WIA service when it intends to transfer data from the device to an application. The WIA driver should determine which type of transfer (via the WIA service) the application is attempting, by reading the **tymed** member of the [**MINIDRV_TRANSFER_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_minidrv_transfer_context):

The **tymed** member, which is set by the application, can have one of the following four values:

TYMED_FILE  
Transfer data to a file.

TYMED_MULTIPAGE_FILE  
Transfer data to a multipage file format.

TYMED_CALLBACK  
Transfer data to memory.

TYMED_MULTIPAGE_CALLBACK  
Transfer multiple pages of data to memory.

The different TYMED settings XXX_CALLBACK and XXX_FILE change the usage of calling the application's callback interface.

### TYMED_CALLBACK and TYMED_MULTIPAGE_CALLBACK

For a memory transfer, issue a [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback) callback:

(*pmdtc->pIWiaMiniDrvCallBack->MiniDrvCallback* in the following sample source code)

Make the callback using the following values:

IT_MSG_DATA  
The driver is transferring data.

IT_STATUS_TRANSFER_TO_CLIENT  
The data transfer message.

*lPercentComplete*  
The percentage of the transfer that is complete.

*pmdtc->cbOffset*  
Update this to the current location where the application should write the next data chunk.

*lBytesReceived*  
The number of bytes in the data chunk being sent to the application.

*pmdtc*  
Pointer to a [**MINIDRV_TRANSFER_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_minidrv_transfer_context) structure that contains the data transfer values.

### TYMED_FILE and TYMED_MULTIPAGE_FILE

For a file transfer, issue a [**IWiaMiniDrvCallBack::MiniDrvCallback**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrvcallback-minidrvcallback) callback::

(*pmdtc->pIWiaMiniDrvCallBack->MiniDrvCallback* in the following sample source code)

Make the callback using the following values.

IT_MSG_STATUS  
The driver is sending status only (no data).

IT_STATUS_TRANSFER_TO_CLIENT  
The data transfer message.

*lPercentComplete*  
The percentage of the transfer that is complete.

If the **ItemSize** member of the MINIDRV_TRANSFER_CONTEXT structure is set to zero, this indicates to the application that the WIA driver does not know the resulting image size and will then allocate its own data buffers. The WIA driver will read the [**WIA_IPA_BUFFER_SIZE**](./wia-ipa-buffer-size.md) property and allocate memory for a single band of data. The WIA driver can allocate any amount of memory it needs here, but it is recommended that allocation be kept small.

To see if the WIA service has allocated memory for the driver, check the *pmdtc->bClassDrvAllocBuf* flag. If it is set to **TRUE**, then the WIA service has allocated memory for the driver. To find out how much memory was allocated, check the value in *pmdtc->lBufferSize*.

To allocate your own memory, use **CoTaskMemAlloc** (described in the Microsoft Windows SDK documentation), and use the pointer located in *pmdtc->pTransferBuffer*. (Remember that the driver allocated this memory, so the driver must also free it.) Set *pmdtc->lBufferSize* to the size you allocated. As previously stated, this WIA sample driver allocates a buffer whose size, in bytes, is equal to the value contained in [**WIA_IPA_BUFFER_SIZE**](./wia-ipa-buffer-size.md). The driver then uses that memory.

The following example shows an implementation of the **IWiaMiniDrv::drvAcquireItemData** method. This example can handle both memory allocation cases.

```cpp
HRESULT _stdcall CWIADevice::drvAcquireItemData(
  BYTE                      *pWiasContext,
  LONG                      lFlags,
  PMINIDRV_TRANSFER_CONTEXT pmdtc,
  LONG                      *plDevErrVal)
{
  //
  // If the caller did not pass in the correct parameters,
  // then fail the call with E_INVALIDARG.
  //

  if (!pWiasContext) {
    return E_INVALIDARG;
  }

  if (!pmdtc) {
    return E_INVALIDARG;
  }

  if (!plDevErrVal) {
    return E_INVALIDARG;
  }

  *plDevErrVal = 0;

  HRESULT hr = E_FAIL;
  LONG lBytesTransferredToApplication = 0;
  LONG lClassDrvAllocSize = 0;
  //
  // (1) Memory allocation
  //

  if (pmdtc->bClassDrvAllocBuf) {

    //
    // WIA allocated the buffer for data transfers
    //

    lClassDrvAllocSize = pmdtc->lBufferSize;
    hr = S_OK;
  } else {

    //
    // Driver allocated the buffer for data transfers
    //

    hr = wiasReadPropLong(pWiasContext, WIA_IPA_BUFFER_SIZE, &lClassDrvAllocSize,NULL,TRUE);
    if (FAILED(hr)) {

      //
      // no memory was allocated, here so we can return early
      //

      return hr;
    }

    //
    // allocate memory of WIA_IPA_BUFFER_SIZE (own min buffer size)
    //

    pmdtc->pTransferBuffer = (PBYTE) CoTaskMemAlloc(lClassDrvAllocSize);
    if (!pmdtc->pTransferBuffer) {

      //
      // no memory was allocated, here so we can return early
      //

      return E_OUTOFMEMORY;
    }

    //
    // set the lBufferSize member
    //

    pmdtc->lBufferSize = lClassDrvAllocSize;
  }

  //
  // (2) Gather all information about data transfer settings and
  //     calculate the total data amount to transfer
  //

  if (hr == S_OK) {
    //
    // WIA service will populate the MINIDRV_TRANSFER_CONTEXT by reading the WIA properties.
    //
    // The following values will be written as a result of the 
    // wiasGetImageInformation() call
    //
    // pmdtc->lWidthInPixels
    // pmdtc->lLines
    // pmdtc->lDepth
    // pmdtc->lXRes
    // pmdtc->lYRes
    // pmdtc->lCompression
    // pmdtc->lItemSize
    // pmdtc->guidFormatID
    // pmdtc->tymed
    //
    // if the FORMAT is set to BMP or MEMORYBMP, the
    // following values will also be set automatically
    //
    // pmdtc->cbWidthInBytes
    // pmdtc->lImageSize
    // pmdtc->lHeaderSize
    // pmdtc->lItemSize (will be updated using the known image format information)
    //

    hr = wiasGetImageInformation(pWiasContext,0,pmdtc);
    if (hr == S_OK) {

      //
      // (3) Send the image data to the application
      //

      LONG lDepth = 0;
      hr = wiasReadPropLong(pWiasContext, WIA_IPA_DEPTH, &lDepth,NULL,TRUE);
      if (hr == S_OK) {

        LONG lPixelsPerLine = 0;
        hr = wiasReadPropLong(pWiasContext, WIA_IPA_PIXELS_PER_LINE, &lPixelsPerLine,NULL,TRUE);
        if (hr == S_OK) {

            LONG lBytesPerLineRaw     = ((lPixelsPerLine * lDepth) + 7) / 8;
            LONG lBytesPerLineAligned = (lPixelsPerLine * lDepth) + 31;
            lBytesPerLineAligned      = (lBytesPerLineAligned / 8) & 0xfffffffc;
            LONG lTotalImageBytes     = pmdtc->lImageSize + pmdtc->lHeaderSize;
            LONG lBytesReceived       = pmdtc->lHeaderSize;
            lBytesTransferredToApplication = 0;
            pmdtc->cbOffset = 0;

            while ((lBytesReceived)) {

              LONG lPercentComplete = (LONG)(((float)lBytesTransferredToApplication/(float)lTotalImageBytes) * 100.0f);
              switch (pmdtc->tymed) {
              case TYMED_MULTIPAGE_CALLBACK:
              case TYMED_CALLBACK:
                {
                  hr = pmdtc->pIWiaMiniDrvCallBack->MiniDrvCallback(IT_MSG_DATA,IT_STATUS_TRANSFER_TO_CLIENT,
                                                                  lPercentComplete,pmdtc->cbOffset,lBytesReceived,pmdtc,0);
                pmdtc->cbOffset += lBytesReceived;
                lBytesTransferredToApplication += lBytesReceived;
           }
            break;
          case TYMED_MULTIPAGE_FILE:
          case TYMED_FILE:
            {
                //
                // lItemSize is the amount that wiasWriteBufToFile will write to FILE
                //

                pmdtc->lItemSize = lBytesReceived;
                hr = wiasWriteBufToFile(0,pmdtc);
                if (FAILED(hr)) {
                    break;
                }

                hr = pmdtc->pIWiaMiniDrvCallBack->MiniDrvCallback(IT_MSG_STATUS,IT_STATUS_TRANSFER_TO_CLIENT,
                                                                  lPercentComplete,0,0,NULL,0);
                lBytesTransferredToApplication += lBytesReceived;
              }
              break;
          default:
              {
          hr = E_FAIL;
              }
              break;
          }

          //
          // scan from device, requesting ytesToReadFromDevice
          //

          LONG lBytesRemainingToTransfer = (lTotalImageBytes - lBytesTransferredToApplication);
          if (lBytesRemainingToTransfer <= 0) {
              break;
            }

            //
            // calculate number of bytes to request from device
            //

            LONG lBytesToReadFromDevice = (lBytesRemainingToTransfer > pmdtc->lBufferSize) ? pmdtc->lBufferSize : lBytesRemainingToTransfer;

            // RAW data request
            lBytesToReadFromDevice = (lBytesToReadFromDevice / lBytesPerLineAligned) * lBytesPerLineRaw;

            // Aligned data request
            // lBytesToReadFromDevice = (lBytesToReadFromDevice / lBytesPerLineAligned) * lBytesPerLineAligned;

            if ((hr == S_FALSE)||FAILED(hr)) {

              //
              // user canceled or the callback failed for some reason
              //

              break;
            }

            //
            // request byte amount from device
            //

            hr = GetDataFromMyDevice(pmdtc->pTransferBuffer, lBytesToReadFromDevice, (DWORD*)&lBytesReceived);
            if (FAILED(hr)) {
                break;
            }

            //
            // this device returns raw data.  If your device does this too, then you should call the AlignInPlace
            // helper function to align the data.
            //

            lBytesReceived = AlignMyRawData(pmdtc->pTransferBuffer,lBytesReceived,lBytesPerLineAligned,lBytesPerLineRaw);

          } // while ((lBytesReceived))
        }
      }
    }
  }

  //
  // free any allocated memory for buffers
  //

  if (!pmdtc->bClassDrvAllocBuf) {
    CoTaskMemFree(pmdtc->pTransferBuffer);
    pmdtc->pTransferBuffer = NULL;
    pmdtc->lBufferSize = 0;
  }

  return hr;
}
```
