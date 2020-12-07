---
title: Other Data Spaces
description: Other Data Spaces
keywords: ["Debugger Engine API, memory, data spaces"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Other Data Spaces


## <span id="ddk_other_data_spaces_dbx"></span><span id="DDK_OTHER_DATA_SPACES_DBX"></span>


In kernel-mode debugging, it is possible to read and write data to a variety of data spaces in addition to the main memory and registers. The following data spaces can be accessed:

<span id="System_Bus"></span><span id="system_bus"></span><span id="SYSTEM_BUS"></span>System Bus  
The methods [**ReadBusData**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readbusdata) and [**WriteBusData**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writebusdata) read and write system bus data.

<span id="Control-Space_Memory"></span><span id="control-space_memory"></span><span id="CONTROL-SPACE_MEMORY"></span>Control-Space Memory  
The methods [**ReadControl**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readcontrol) and [**WriteControl**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writecontrol) read and write control-space memory.

<span id="i_o_memory."></span><span id="I_O_MEMORY."></span>I/O Memory.  
The methods [**ReadIo**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readio) and [**WriteIo**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-writeio) read and write system and bus I/O memory.

<span id="Model_Specific_Register__MSR_"></span><span id="model_specific_register__msr_"></span><span id="MODEL_SPECIFIC_REGISTER__MSR_"></span>Model Specific Register (MSR)  
The methods [**ReadMsr**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readmsr) and [**WriteMsr**](/windows-hardware/drivers/ddi/wdbgexts/nf-wdbgexts-writemsr) read and write MSRs, which are control registers that enable and disable features, and support debugging, for a particular model of CPU.

### <span id="handles"></span><span id="HANDLES"></span> Handles

In user-mode debugging, information about system objects can be obtained using system handles owned by a target process. The method [**ReadHandleData**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugdataspaces4-readhandledata) can be used to read this information.

System handles for thread and process system objects can be obtained by using the [**GetCurrentThreadHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects4-getcurrentthreadhandle) and [**GetCurrentProcessHandle**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsystemobjects-getcurrentprocesshandle) methods. These handles are also provided to the [**IDebugEventCallbacks::CreateThread**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-createthread) and [**IDebugEventCallbacks::CreateProcess**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugeventcallbacks-createprocess) callback methods when create-thread and create-process debugging event occur.

**Note**   In kernel mode, the process and thread handles are artificial handles. They are not system handles.

 

 

