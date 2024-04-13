---
title: Client Objects and the Engine
description: Client Objects and the Engine
keywords: ["EngExtCpp extensions, client objects"]
ms.date: 05/23/2017
---

# Client Objects and the Engine


## <span id="ddk_using_clients_and_the_engine_dbx"></span><span id="DDK_USING_CLIENTS_AND_THE_ENGINE_DBX"></span>


An EngExtCpp extension interacts with the [debugger engine](introduction.md#debugger-engine) through a client object. Interface pointers to the client object are available to the extension through members of the [**ExtExtension**](/previous-versions/ff543981(v=vs.85)) base class. The following members provide access to the first version of the engine API interfaces.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Engine API interface</th>
<th align="left">ExtExtension member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugadvanced" data-raw-source="[IDebugAdvanced](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugadvanced)">IDebugAdvanced</a></p></td>
<td align="left"><p><strong>m_Advanced</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugclient" data-raw-source="[IDebugClient](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugclient)">IDebugClient</a></p></td>
<td align="left"><p><strong>m_Client</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugcontrol" data-raw-source="[IDebugControl](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugcontrol)">IDebugControl</a></p></td>
<td align="left"><p><strong>m_Control</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugdataspaces" data-raw-source="[IDebugDataSpaces](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugdataspaces)">IDebugDataSpaces</a></p></td>
<td align="left"><p><strong>m_Data</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugregisters" data-raw-source="[IDebugRegisters](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugregisters)">IDebugRegisters</a></p></td>
<td align="left"><p><strong>m_Registers</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugsymbols" data-raw-source="[IDebugSymbols](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugsymbols)">IDebugSymbols</a></p></td>
<td align="left"><p><strong>m_Symbols</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugsystemobjects" data-raw-source="[IDebugSystemObjects](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugsystemobjects)">IDebugSystemObjects</a></p></td>
<td align="left"><p><strong>m_System</strong></p></td>
</tr>
</tbody>
</table>

 

The following members provide access to later versions of the engine API interfaces. These interfaces may not be available in all versions of the debugger engine. If they are not available, any attempt to use them will result in a exception being thrown.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Engine API interface</th>
<th align="left">ExtExtension member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>IDebugAdvanced2</strong></p></td>
<td align="left"><p><strong>m_Advanced2</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugAdvanced3</strong></p></td>
<td align="left"><p><strong>m_Advanced3</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugClient2</strong></p></td>
<td align="left"><p><strong>m_Client2</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugClient3</strong></p></td>
<td align="left"><p><strong>m_Client3</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugClient4</strong></p></td>
<td align="left"><p><strong>m_Client4</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugClient5</strong></p></td>
<td align="left"><p><strong>m_Client5</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugControl2</strong></p></td>
<td align="left"><p><strong>m_Control2</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugControl3</strong></p></td>
<td align="left"><p><strong>m_Control3</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugControl4</strong></p></td>
<td align="left"><p><strong>m_Control4</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugData2</strong></p></td>
<td align="left"><p><strong>m_Data2</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugData3</strong></p></td>
<td align="left"><p><strong>m_Data3</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugData4</strong></p></td>
<td align="left"><p><strong>m_Data4</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugRegisters2</strong></p></td>
<td align="left"><p><strong>m_Registers2</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugSymbols2</strong></p></td>
<td align="left"><p><strong>m_Symbols2</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugSymbols3</strong></p></td>
<td align="left"><p><strong>m_Symbols3</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugSystemObjects2</strong></p></td>
<td align="left"><p><strong>m_System2</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IDebugSystemObjects3</strong></p></td>
<td align="left"><p><strong>m_System3</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IDebugSystemObjects4</strong></p></td>
<td align="left"><p><strong>m_System4</strong></p></td>
</tr>
</tbody>
</table>

 

The members in these tables are initialized each time the extension library is used to execute an extension command or format a structure for output. Once a task is completed, these members are uninitialized. Consequently, extensions should not cache the values of these members and should use the **ExtExtension** members directly.

An extension library can also create its own client objects using the method [**IDebugClient::CreateClient**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-createclient) or the functions [**DebugCreate**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-debugcreate) or [**DebugConnect**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-debugconnect).

For an overview of client objects, see [Client Objects](client-objects.md).

