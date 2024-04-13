---
title: Vendor-extended Commands
description: Vendor-extended commands
ms.date: 05/02/2023
---

# Vendor-extended commands

An application can send an arbitrary command to the device through the **IWiaItemExtras::Escape** method, which is described in the Microsoft Windows SDK documentation. By calling **QueryInterface** on the root item, you can retrieve a pointer to the **IWiaItemExtras** interface. The application can then construct a PTP command using any opcode and parameters, and send this command to the device. The application also can send data to or receive data from the device.

The device informs the application of the outcome of the operation when the **IWiaItemExtras::Escape** method returns, filling in a response code and response parameters in a [**PTP_VENDOR_DATA_OUT**](/windows-hardware/drivers/ddi/ptpusd/ns-ptpusd-_ptp_vendor_data_out) structure. The **SessionId** and **TransactionId** members of the [**PTP_VENDOR_DATA_IN**](/windows-hardware/drivers/ddi/ptpusd/ns-ptpusd-_ptp_vendor_data_in) structure are ignored. The driver supplies correct values for these.

For vendor-defined commands other than ESCAPE_PTP_CLEAR_STALLS, a special flag, ESCAPE_PTP_VENDOR_COMMAND, must be combined (using an OR operator) with the command used in the **IWiaItemExtras::Escape** method. If a vendor-defined command creates or deletes an object on the device using the following described flags, the driver adds or removes the object from its internal structures and generates a WIA event. All other standard commands should be issued through the appropriate WIA interface.

The first parameter to **IWiaItemExtras::Escape** is the combination of one or more of the following flags:

| Escape Code | Meaning |
|--|--|
| ESCAPE_PTP_ADD_OBJ_CMD | An object is being added and the handle for the object is in one of the command parameters. |
| ESCAPE_PTP_REM_OBJ_CMD | An object is being removed and the handle for the object is in one of the command parameters. |
| ESCAPE_PTP_ADD_OBJ_RESP | An object is being added and the handle for the object is in one of the response parameters. |
| ESCAPE_PTP_REM_OBJ_RESP | An object is being removed and the handle for the object is in one of the response parameters. |
| ESCAPE_PTP_ADDREM_PARM1 | The handle for the added or removed object is in the first parameter of the command or response. |
| ESCAPE_PTP_ADDREM_PARM2 | The handle for the added or removed object is in the second parameter of the command or response. |
| ESCAPE_PTP_ADDREM_PARM3 | The handle for the added or removed object is in the third parameter of the command or response. |
| ESCAPE_PTP_ADDREM_PARM4 | The handle for the added or removed object is in the fourth parameter of the command or response. |
| ESCAPE_PTP_ADDREM_PARM5 | The handle for the added or removed object is in the fifth parameter of the command or response. |
| ESCAPE_PTP_CLEAR_STALLS | Clear any error conditions caused by a vendor-extended command. This flag cannot be used in combination with any of the other flags. For more information about this flag, see the note that follows this table. |
| ESCAPE_PTP_VENDOR_COMMAND | The command is a vendor-extended command. |

When an application calls **IWiaItemExtras::Escape** with the ESCAPE_PTP_CLEAR_STALL flag as the first argument to this method, the driver issues the PTP **Get Device Status** request to determine whether any endpoints are in a STALL condition. If the **Get Device Status** command succeeds, the driver issues the [**IOCTL_RESET_PIPE**](/windows-hardware/drivers/ddi/usbscan/ni-usbscan-ioctl_reset_pipe) USB control code for each such endpoint. If the **Get Device Status** command fails, the driver issues a PTP **Device Reset** request. **Get Device Status** and **Device Reset** are described in the PIMA 15740:2000 standard, First Edition, and Revision 1.0 of the USB Still Image Capture Device Definition (USB SICDD).

The following sample code illustrates how to use the vendor-extended command interface. Be sure that your code includes the *ptpusd.h* header, because it contains the definitions of the escape codes and other constants, and the [**PTP_VENDOR_DATA_IN**](/windows-hardware/drivers/ddi/ptpusd/ns-ptpusd-_ptp_vendor_data_in) and [**PTP_VENDOR_DATA_OUT**](/windows-hardware/drivers/ddi/ptpusd/ns-ptpusd-_ptp_vendor_data_out) structures. The **IWiaItemExtras** interface is obtained by using a call to **QueryInterface** on the root item. A pointer to this root item, *pIWiaRootItem*, can be obtained, for example, by a call to **IWiaDevMgr::SelectDeviceDlg** (described in the Microsoft Windows SDK documentation).

```cpp
//
// Test IWiaItemExtras::Escape method
//
HRESULT hr = S_OK;
IWiaItemExtras *pIWiaItemExtras = NULL;

hr = pIWiaRootItem->QueryInterface(IID_IWiaItemExtras,
                                   (VOID **) &pIWiaItemExtras);
if (FAILED(hr)) {
    MessageBox("QueryInterface for IWiaItemExtras failed");
    return;
}

PTP_VENDOR_DATA_IN *pDataIn = NULL;
PTP_VENDOR_DATA_OUT *pDataOut = NULL;
DWORD dwDataInSize = SIZEOF_REQUIRED_VENDOR_DATA_IN;
DWORD dwDataOutSize = SIZEOF_REQUIRED_VENDOR_DATA_OUT + 0x1000;
DWORD dwActualDataOutSize = 0;

pDataIn = (PTP_VENDOR_DATA_IN *) CoTaskMemAlloc(dwDataInSize);
if (!pDataIn) {
    MessageBox("CoTaskMemAlloc failed");
    return;
}

pDataOut = (PTP_VENDOR_DATA_OUT *) CoTaskMemAlloc(dwDataOutSize);
if (!pDataOut) {
 CoTaskMemFree(pDataIn);
    MessageBox("CoTaskMemAlloc failed");
    return;
}
ZeroMemory(pDataIn, dwDataInSize);
ZeroMemory(pDataOut, dwDataOutSize);

pDataIn->OpCode = 0x1001;
pDataIn->SessionId = 0;     // The driver will fill this in.
pDataIn->TransactionId = 0; // The driver will fill this in.
pDataIn->NumParams = 0;

//
// pDataIn->NextPhase informs the PTP driver whether to 
// read data from the device (as shown), or
// write data to the device (use PTP_NEXTPHASE_WRITE_DATA),
// to neither read nor write data (use PTP_NEXTPHASE_NO_DATA).
//
pDataIn->NextPhase = PTP_NEXTPHASE_READ_DATA;

hr = pIWiaItemExtras->Escape(ESCAPE_PTP_VENDOR_COMMAND,
                             (BYTE *) pDataIn, dwDataInSize,
                             (BYTE *) pDataOut, dwDataOutSize,
                             &dwActualDataOutSize);

if (FAILED(hr)) {
    MessageBox("Escape failed");
    return;
}

//
// Data returned from device is located at pDataOut->VendorReadData.
//
```
