---
title: Other Data Spaces
description: Other Data Spaces
ms.assetid: f676a478-c02a-4400-8173-a1b3103c6c1b
keywords: ["Debugger Engine API, memory, data spaces"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Other Data Spaces


## <span id="ddk_other_data_spaces_dbx"></span><span id="DDK_OTHER_DATA_SPACES_DBX"></span>


In kernel-mode debugging, it is possible to read and write data to a variety of data spaces in addition to the main memory and registers. The following data spaces can be accessed:

<span id="System_Bus"></span><span id="system_bus"></span><span id="SYSTEM_BUS"></span>System Bus  
The methods [**ReadBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-readbusdata) and [**WriteBusData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-writebusdata) read and write system bus data.

<span id="Control-Space_Memory"></span><span id="control-space_memory"></span><span id="CONTROL-SPACE_MEMORY"></span>Control-Space Memory  
The methods [**ReadControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-readcontrol) and [**WriteControl**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-writecontrol) read and write control-space memory.

<span id="i_o_memory."></span><span id="I_O_MEMORY."></span>I/O Memory.  
The methods [**ReadIo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-readio) and [**WriteIo**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-writeio) read and write system and bus I/O memory.

<span id="Model_Specific_Register__MSR_"></span><span id="model_specific_register__msr_"></span><span id="MODEL_SPECIFIC_REGISTER__MSR_"></span>Model Specific Register (MSR)  
The methods [**ReadMsr**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-readmsr) and [**WriteMsr**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdbgexts/nf-wdbgexts-writemsr) read and write MSRs, which are control registers that enable and disable features, and support debugging, for a particular model of CPU.

### <span id="handles"></span><span id="HANDLES"></span> Handles

In user-mode debugging, information about system objects can be obtained using system handles owned by a target process. The method [**ReadHandleData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugdataspaces4-readhandledata) can be used to read this information.

System handles for thread and process system objects can be obtained by using the [**GetCurrentThreadHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle) and [**GetCurrentProcessHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle) methods. These handles are also provided to the [**IDebugEventCallbacks::CreateThread**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugeventcallbacks-createthread) and [**IDebugEventCallbacks::CreateProcess**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dbgeng/nf-dbgeng-idebugeventcallbacks-createprocess) callback methods when create-thread and create-process debugging event occur.

**Note**   In kernel mode, the process and thread handles are artificial handles. They are not system handles.

 

 

 





