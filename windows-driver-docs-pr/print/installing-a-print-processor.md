---
title: Installing a Print Processor
author: windows-driver-content
description: Installing a Print Processor
MS-HAID:
- 'provider\_76db69e3-3b07-49f9-af34-8c002c0bb696.xml'
- 'print.installing\_a\_print\_processor'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4e9e1148-16a3-42f6-a262-1eef014636d0
keywords: ["print processors WDK , installing", "installing print processors WDK", "print queues WDK , print processor installations", "associating print processor with print queue WDK", "print processors WDK , associating with print queue", "print queues WDK"]
---

# Installing a Print Processor


## <a href="" id="ddk-installing-a-print-processor-gg"></a>


To install a print processor, an installation application must call the spooler's **AddPrintProcessor** function. To associate a print processor with a print queue, list its file name in an INF file in a PrintProcessor entry. This entry must be included for every print queue to which the print processor is to be associated. For more information, see [Printer INF Files](printer-inf-files.md).

When an installation application calls the spooler's **AddPrinter** function, using a PRINTER\_INFO\_2 structure as an input argument, it specifies the print processor name (obtained from the INF file) as a structure member. (The **AddPrintProcessor** and **AddPrinter** functions and the PRINTER\_INFO\_2 structure are described in the Microsoft Windows SDK documentation.)

### Associating a Print Processor with a PnP-installed Print Queue

If the Plug and Play (PnP) manager detects and installs a print queue on a system running either Windows 2000 or Windows XP, and if the INF file used to install the print queue contains a PrintProcessor entry other than the default Windows print processor, WinPrint, the print processor will not be associated with the print queue. However, the print processor will be installed. (Note that if you install the print queue using the Add Printer wizard, the print processor is correctly associated with the print queue. Note also that the PnP manager in Microsoft Windows Server 2003 and later correctly associates a print processor with the print queue.)

To associate the print processor with the print queue for Plug and Play installations on Windows 2000 and Windows XP, include a PRINTER\_EVENT\_INITIALIZE case in the printer interface DLL's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function. For Microsoft Windows Server 2003 and later, it is not necessary to add a PRINTER\_EVENT\_INITIALIZE case in the **DrvPrinterEvent** function.

The following code example sets the **pPrintProcessor** member of the PRINTER\_INFO\_2 structure to the name of your print processor, and then calls the **SetPrinter** function (described in the Windows SDK documentation) to update the printer's settings. Note that the name of the print processor in *gszPrintProc* must be the same as that in the PrintProcessor entry in your INF file.

```
BOOL
DrvPrinterEvent(
               LPWSTR  pPrinterName,
               INT     Event,
               DWORD   Flags,
               LPARAM  lParam
               )

{
  PRINTER_DEFAULTS  PrinterDef = {NULL, NULL, PRINTER_ALL_ACCESS};
  HANDLE            hPrinter;
  LPPRINTER_INFO_2  pInfo = NULL;
  DWORD             cbNeeded;
  TCHAR             gszPrintProc[] = TEXT("<Print processor name>");
  BOOL              bRet = TRUE;

  switch (Event)
  {
    case PRINTER_EVENT_INITIALIZE:
      if (OpenPrinter(pPrinterName, &hPrinter, &PrinterDef))
      {
        if ( !GetPrinter( hPrinter, 2, (LPBYTE) pInfo, 0, &cbNeeded ) &&
           (GetLastError() != ERROR_INSUFFICIENT_BUFFER) )
        {
          bRet = FALSE;
        }
        if (bRet == TRUE)
        {
          pInfo = (LPPRINTER_INFO_2) LocalAlloc(LPTR, cbNeeded);
          bRet = pInfo ? TRUE : FALSE;
        }
        if (bRet == TRUE)
        {
          if (GetPrinter(hPrinter, 2, (LPBYTE) pInfo, cbNeeded, &cbNeeded))
          {
            pInfo->pPrintProcessor = gszPrintProc;
            SetPrinter(hPrinter, 2, (LPBYTE) pInfo, 0);
          }
          else 
          {
            bRet = FALSE;
          }
          if (pInfo)
          {
            LocalFree(pInfo);
          }
        }
        ClosePrinter(hPrinter);
      }
      else  // OpenPrinter failed
      {
        bRet = FALSE;
      }
    break;
    // cases for other events

    default:
      break;
  }  // end switch
  return bRet;
}
```

### <a href="" id="associating-a-print-processor-with-a-print-queue-during-printer-driver"></a>Associating a Print Processor with a Print Queue During Printer Driver Upgrade

When a printer driver is updated, the print processor of the updated print queue is not changed. If the new printer driver requires a particular print processor, the printer interface DLL's [**DrvUpgradePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff548648) function must set the **pPrintProcessor** member of the PRINTER\_INFO\_2 structure to the name of the new print processor. After this occurs, this function calls **SetPrinter** to update the printer's settings. The spooler calls the **DrvUpgradePrinter** function once for each printer, which ensures that all printers using that driver also use the required print processor. The following code example demonstrates these points.

```
BOOL
DrvUpgradePrinter(
                 DWORD   Level,
                 LPBYTE  pDriverUpgradeInfo
                 )
{
  HANDLE                  hPrinter;
  PRINTER_DEFAULTS        PrinterDef = {NULL, NULL, PRINTER_ALL_ACCESS};
 PDRIVER_UPGRADE_INFO_2  pDUI2;
  LPPRINTER_INFO_2        pInfo = NULL;
 DWORD                   cbNeeded;
  TCHAR                   gszPrintProc[]   = TEXT("<Print processor name>");
  TCHAR                   gszPrintDriver[] = TEXT("<Printer driver name>");
  BOOL                    bRet = TRUE;

  if ((Level == 2)                                            &&
      (pDUI2 = (PDRIVER_UPGRADE_INFO_2)pDriverUpgradeInfo)    &&
      (OpenPrinter(pDUI2->pPrinterName, &hPrinter, &PrinterDef)))
  {
    if ( !GetPrinter( hPrinter, 2, (LPBYTE) pInfo, 0, &cbNeeded )  &&
         (GetLastError() != ERROR_INSUFFICIENT_BUFFER) )
    {
       bRet = FALSE;
    }
    if (bRet == TRUE)
    {
      pInfo = (LPPRINTER_INFO_2) LocalAlloc(LPTR, cbNeeded);
      bRet = pInfo ? TRUE : FALSE;
    }
    if (bRet == TRUE)
    {
      if (GetPrinter(hPrinter, 2, (LPBYTE) pInfo, cbNeeded, &cbNeeded))
      {
      //
      // This function is called for every printer queue that uses a driver
      // for which one or more files were updated. However, we only want to
      // update the printer queue&#39;s "driver" by a particular driver.
      //
      if ( !lstrcmpi(pInfo->pDriverName, gszPrintDriver) )
      {
        pInfo->pPrintProcessor =  gszPrintProc;
        SetPrinter(hPrinter, 2, (LPBYTE) pInfo, 0);
      }
    else  // GetPrinter 
    {
      bRet = FALSE;
    }
    if (pInfo)
    {
      LocalFree(pInfo);
    }
    ClosePrinter(hPrinter);
  }
  else  // Level != 2 or pDUI2 == NULL or OpenPrinter failed
  {
    bRet = FALSE;
  }
  return bRet;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20Print%20Processor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


