---
title: IrqlZwPassive rule (wdm)
description: The IrqlZwPassive rule specifies that the driver calls ZwClose only when it is executing at IRQL PASSIVE_LEVEL.
ms.assetid: d31612ad-e869-4fc7-bc09-e5b4d5362585
ms.date: 05/21/2018
keywords: ["IrqlZwPassive rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlZwPassive
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlZwPassive rule (wdm)


The **IrqlZwPassive** rule specifies that the driver calls [**ZwClose**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) only when it is executing at IRQL = PASSIVE\_LEVEL.

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x2001F)


Example
-------

The following code violates this rule:

``` syntax
NTSTATUS 
DriverCloseResources (
    _In_ PDRIVER_CONTEXT Context
    )
{
    …

    NT_ASSERT(KeGetCurrentIrql() == PASSIVE_LEVEL);

    //
    // ExAcquireFastMutex sets the IRQL to APC_LEVEL, and the caller continues 
    // to run at APC_LEVEL after ExAcquireFastMutex returns.
    //
  
    ExAcquireFastMutex(&Context->FastMutex);
    
    ....
    
    if (NULL != Context->Handle) {

            //
            // RULE VIOLATION! - ZwClose can be called only at PASSIVE_LEVEL 
            //
            
            ZwClose(Context->Handle);      
            Context->Handle = NULL;
    }
    
    ....

    //
    // N.B. ExReleaseFastMutex restores the original IRQL.
    //
     
    ExReleaseFastMutex(&Context->FastMutex);
    
    ....
}
```

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>IrqlZwPassive</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/driver-verifier)">Driver Verifier</a> and select the <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**ZwClose**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose)
[**ZwCreateKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey)
[**ZwDeleteKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwdeletekey)
[**ZwEnumerateKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratekey)
[**ZwEnumerateValueKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwenumeratevaluekey)
[**ZwFlushKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwflushkey)
[**ZwOpenKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey)
[**ZwQueryKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwquerykey)
[**ZwQueryValueKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwqueryvaluekey)
[**ZwSetValueKey**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-zwsetvaluekey)
 

 





