---
title: Installing a Print Processor
description: Installing a Print Processor
ms.assetid: 4e9e1148-16a3-42f6-a262-1eef014636d0
keywords:
- print processors WDK , installing
- installing print processors WDK
- print queues WDK , print processor installations
- associating print processor with print queue WDK
- print processors WDK , associating with print queue
- print queues WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Print Processor





To install a print processor, an installation application must call the spooler's **AddPrintProcessor** function. To associate a print processor with a print queue, list its file name in an INF file in a PrintProcessor entry. This entry must be included for every print queue to which the print processor is to be associated. For more information, see [Printer INF Files](printer-inf-files.md).

When an installation application calls the spooler's **AddPrinter** function, using a PRINTER\_INFO\_2 structure as an input argument, it specifies the print processor name (obtained from the INF file) as a structure member. (The **AddPrintProcessor** and **AddPrinter** functions and the PRINTER\_INFO\_2 structure are described in the Microsoft Windows SDK documentation.)

### Associating a Print Processor with a PnP-installed Print Queue

If the Plug and Play (PnP) manager detects and installs a print queue on a system running either Windows 2000 or Windows XP, and if the INF file used to install the print queue contains a PrintProcessor entry other than the default Windows print processor, WinPrint, the print processor will not be associated with the print queue. However, the print processor will be installed. (Note that if you install the print queue using the Add Printer wizard, the print processor is correctly associated with the print queue. Note also that the PnP manager in Microsoft Windows Server 2003 and later correctly associates a print processor with the print queue.)

To associate the print processor with the print queue for Plug and Play installations on Windows 2000 and Windows XP, include a PRINTER\_EVENT\_INITIALIZE case in the printer interface DLL's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function. For Microsoft Windows Server 2003 and later, it is not necessary to add a PRINTER\_EVENT\_INITIALIZE case in the **DrvPrinterEvent** function.

The following code example sets the **pPrintProcessor** member of the PRINTER\_INFO\_2 structure to the name of your print processor, and then calls the **SetPrinter** function (described in the Windows SDK documentation) to update the printer's settings. Note that the name of the print processor in *gszPrintProc* must be the same as that in the PrintProcessor entry in your INF file.

```cpp
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

```cpp
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
      // update the printer queue's "driver" by a particular driver.
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

 

 




