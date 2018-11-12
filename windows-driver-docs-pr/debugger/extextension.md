---
title: ExtExtension
description: The ExtExtension class is the base class for the C++ class that represents the EngExtCpp extension library.
ms.assetid: 9c6c4633-df49-4f49-8116-d680bb20c3f5
keywords: ["ExtExtension Windows Debugging"]
topic_type:
- apiref
api_name:
- ExtExtension
api_type:
- NA
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ExtExtension


The **ExtExtension** class is the base class for the C++ class that represents the EngExtCpp extension library.

The **ExtExtension** class includes the following methods, which can be used by the subclass:

[**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff550945)

[**Uninitialize**](https://msdn.microsoft.com/library/windows/hardware/ff558961)

[**OnSessionActive**](https://msdn.microsoft.com/library/windows/hardware/ff552312)

[**OnSessionInactive**](https://msdn.microsoft.com/library/windows/hardware/ff552318)

[**OnSessionAccessible**](https://msdn.microsoft.com/library/windows/hardware/ff552310)

[**OnSessionInaccessible**](https://msdn.microsoft.com/library/windows/hardware/ff552315)

**IsUserMode**

**IsKernelMode**

**IsLiveLocalUser**

**IsMachine32**

**IsCurMachine32**

**IsMachine64**

**IsCurMachine64**

**Is32On64**

**CanQueryVirtual**

**HasFullMemBasic**

**IsExtensionRemote**

**AreOutputCallbacksDmlAware**

**RequireUserMode**

**RequireKernelMode**

[**GetNumUnnamedArgs**](https://msdn.microsoft.com/library/windows/hardware/ff548001)

[**GetUnnamedArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff549464)

[**GetUnnamedArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff549465)

[**HasUnnamedArg**](https://msdn.microsoft.com/library/windows/hardware/ff549733)

[**GetArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff545586)

[**GetArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff545596)

[**HasArg**](https://msdn.microsoft.com/library/windows/hardware/ff549721)

[**HasCharArg**](https://msdn.microsoft.com/library/windows/hardware/ff549727)

[**SetUnnamedArg**](https://msdn.microsoft.com/library/windows/hardware/ff556876)

[**SetUnnamedArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff556878)

[**SetUnnamedArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff556879)

[**SetArg**](https://msdn.microsoft.com/library/windows/hardware/ff556614)

[**SetArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff556618)

[**SetArgU64**](https://msdn.microsoft.com/library/windows/hardware/ff556622)

[**GetRawArgStr**](https://msdn.microsoft.com/library/windows/hardware/ff548226)

**GetRawArgCopy**

**Out**

**Warn**

**Err**

**Verb**

**Dml**

**DmlWarn**

**DmlErr**

**DmlVerb**

**DmlCmdLink**

**DmlCmdExec**

**RefreshOutputCallbackFlags**

**WrapLine**

**OutWrapStr**

**OutWrapVa**

**OutWrap**

**DemandWrap**

**AllowWrap**

**TestWrap**

**RequestCircleString**

**CopyCircleString**

**PrintCircleStringVa**

**PrintCircleString**

**SetAppendBuffer**

**AppendBufferString**

**AppendStringVa**

**AppendString**

**IsAppendStart**

**SetCallStatus**

**GetCachedSymbolTypeId**

**GetCachedFieldOffset**

**GetCachedFieldOffset**

**AddCachedSymbolInfo**

**GetExpr64**

**GetExprU64**

**GetExprS64**

**ThrowCommandHelp**

**ThrowInterrupt**

**ThrowOutOfMemory**

**ThrowContinueSearch**

**ThrowReloadExtension**

**ThrowInvalidArg**

**ThrowRemote**

**ThrowStatus**

**ThrowLastError**

The **ExtExtension** class also contains the following fields that can be used by the subclass:

```cpp
class ExtExtension
{
public:
    USHORT  m_ExtMajorVersion;
    USHORT  m_ExtMinorVersion;
    ULONG  m_ExtInitFlags;
    ExtKnownStruct *  m_KnownStructs;
    ExtProvidedValue *  m_ProvidedValues;
    ExtCheckedPointer<IDebugAdvanced>  m_Advanced;
    ExtCheckedPointer<IDebugClient>  m_Client;
    ExtCheckedPointer<IDebugControl>  m_Control;
    ExtCheckedPointer<IDebugDataSpaces>  m_Data;
    ExtCheckedPointer<IDebugRegisters>  m_Registers;
    ExtCheckedPointer<IDebugSymbols>  m_Symbols;
    ExtCheckedPointer<IDebugSystemObjects>  m_System;
    ExtCheckedPointer<IDebugAdvanced2>  m_Advanced2;
    ExtCheckedPointer<IDebugAdvanced3>  m_Advanced3;
    ExtCheckedPointer<IDebugClient2>  m_Client2;
    ExtCheckedPointer<IDebugClient3>  m_Client3;
    ExtCheckedPointer<IDebugClient4>  m_Client4;
    ExtCheckedPointer<IDebugClient5>  m_Client5;
    ExtCheckedPointer<IDebugControl2>  m_Control2;
    ExtCheckedPointer<IDebugControl3>  m_Control3;
    ExtCheckedPointer<IDebugControl4>  m_Control4;
    ExtCheckedPointer<IDebugDataSpaces2>  m_Data2;
    ExtCheckedPointer<IDebugDataSpaces3>  m_Data3;
    ExtCheckedPointer<IDebugDataSpaces4>  m_Data4;
    ExtCheckedPointer<IDebugRegisters2>  m_Registers2;
    ExtCheckedPointer<IDebugSymbols2>  m_Symbols2;
    ExtCheckedPointer<IDebugSymbols3>  m_Symbols3;
    ExtCheckedPointer<IDebugSystemObjects2>  m_System2;
    ExtCheckedPointer<IDebugSystemObjects3>  m_System3;
    ExtCheckedPointer<IDebugSystemObjects4>  m_System4;
    ULONG  m_OutputWidth;
    ULONG  m_ActualMachine;
    ULONG  m_Machine;
    ULONG  m_PageSize;
    ULONG  m_PtrSize;
    ULONG  m_NumProcessors;
    ULONG64  m_OffsetMask;
    ULONG  m_DebuggeeClass;
    ULONG  m_DebuggeeQual;
    ULONG  m_DumpFormatFlags;
    bool  m_IsRemote;
    bool  m_OutCallbacksDmlAware;
    ULONG  m_OutMask;
    ULONG  m_CurChar;
    ULONG  m_LeftIndent;
    bool  m_AllowWrap;
    bool  m_TestWrap;
    ULONG  m_TestWrapChars;
    PSTR  m_AppendBuffer;
    ULONG  m_AppendBufferChars;
    PSTR  m_AppendAt;
};
```

## <span id="Members"></span><span id="members"></span><span id="MEMBERS"></span>Members


<span id="m_ExtMajorVersion"></span><span id="m_extmajorversion"></span><span id="M_EXTMAJORVERSION"></span>**m\_ExtMajorVersion**  
The major version number of the extension library. This should be set by the [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff550945) method. If it is not set, it defaults to **1**.

<span id="m_ExtMinorVersion"></span><span id="m_extminorversion"></span><span id="M_EXTMINORVERSION"></span>**m\_ExtMinorVersion**  
The minor version number of the extension library. This should be set by the [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff550945) method. If it is not set, it defaults to **0** (zero).

<span id="m_ExtInitFlags"></span><span id="m_extinitflags"></span><span id="M_EXTINITFLAGS"></span>**m\_ExtInitFlags**  
The DbgEng extension initialization flags for [*DebugExtensionInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff540476).

<span id="m_KnownStructs"></span><span id="m_knownstructs"></span><span id="M_KNOWNSTRUCTS"></span>**m\_KnownStructs**  
An array of [**ExtKnownStruct**](https://msdn.microsoft.com/library/windows/hardware/ff543985) structures that the extension library is capable of formatting for output. This member should be set by the [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff550945) method and should not be changed once this method returns.

If **m\_KnownStructs** is not **NULL**, the **TypeName** member of the last **ExtKnownStruct** structure in the array must be **NULL**.

When formatting a target's structure for output, if the name of the structure's type matches the **TypeName** member of one of the **ExtKnownStruct** structures in this array, the callback function specified in the **Method** member is called to perform the formatting.

<span id="m_ProvidedValues"></span><span id="m_providedvalues"></span><span id="M_PROVIDEDVALUES"></span>**m\_ProvidedValues**  
An array of **ExtProvidedValue** structures listing the pseudo registers that the extension library can provide values for. This member should be set by the [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff550945) method and should not be changed once this method returns.

If **m\_ProvidedValues** is not **NULL**, the **ValueName** member of the last **ExtProvidedValue** structure in the array must be **NULL**.

When evaluating a pseudo register, if the name of the pseudo register matches the **ValueName** member of one of the **ExtProvidedValue** structures in this array, the callback function specified in the **Method** member is called to evaluate the pseudo register.

<span id="m_Advanced"></span><span id="m_advanced"></span><span id="M_ADVANCED"></span>**m\_Advanced**  
The [**IDebugAdvanced**](https://msdn.microsoft.com/library/windows/hardware/ff549798) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_Client"></span><span id="m_client"></span><span id="M_CLIENT"></span>**m\_Client**  
The [**IDebugClient**](https://msdn.microsoft.com/library/windows/hardware/ff549827) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_Control"></span><span id="m_control"></span><span id="M_CONTROL"></span>**m\_Control**  
The [**IDebugControl**](https://msdn.microsoft.com/library/windows/hardware/ff550508) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_Data"></span><span id="m_data"></span><span id="M_DATA"></span>**m\_Data**  
The [**IDebugDataSpaces**](https://msdn.microsoft.com/library/windows/hardware/ff550528) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_Registers"></span><span id="m_registers"></span><span id="M_REGISTERS"></span>**m\_Registers**  
The [**IDebugRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff550825) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_Symbols"></span><span id="m_symbols"></span><span id="M_SYMBOLS"></span>**m\_Symbols**  
The [**IDebugSymbols**](https://msdn.microsoft.com/library/windows/hardware/ff550856) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_System"></span><span id="m_system"></span><span id="M_SYSTEM"></span>**m\_System**  
The [**IDebugSystemObjects**](https://msdn.microsoft.com/library/windows/hardware/ff550875) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**.

<span id="m_Advanced2"></span><span id="m_advanced2"></span><span id="M_ADVANCED2"></span>**m\_Advanced2**  
The [**IDebugAdvanced2**](https://msdn.microsoft.com/library/windows/hardware/ff549798) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Advanced3"></span><span id="m_advanced3"></span><span id="M_ADVANCED3"></span>**m\_Advanced3**  
The [**IDebugAdvanced3**](https://msdn.microsoft.com/library/windows/hardware/ff549798) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Client2"></span><span id="m_client2"></span><span id="M_CLIENT2"></span>**m\_Client2**  
The [**IDebugClient2**](https://msdn.microsoft.com/library/windows/hardware/ff549827) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Client3"></span><span id="m_client3"></span><span id="M_CLIENT3"></span>**m\_Client3**  
The [**IDebugClient3**](https://msdn.microsoft.com/library/windows/hardware/ff549827) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Client4"></span><span id="m_client4"></span><span id="M_CLIENT4"></span>**m\_Client4**  
The [**IDebugClient4**](https://msdn.microsoft.com/library/windows/hardware/ff549827) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Client5"></span><span id="m_client5"></span><span id="M_CLIENT5"></span>**m\_Client5**  
The [**IDebugClient5**](https://msdn.microsoft.com/library/windows/hardware/ff549827) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Control2"></span><span id="m_control2"></span><span id="M_CONTROL2"></span>**m\_Control2**  
The [**IDebugControl2**](https://msdn.microsoft.com/library/windows/hardware/ff550508) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Control3"></span><span id="m_control3"></span><span id="M_CONTROL3"></span>**m\_Control3**  
The [**IDebugControl3**](https://msdn.microsoft.com/library/windows/hardware/ff550508) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Control4"></span><span id="m_control4"></span><span id="M_CONTROL4"></span>**m\_Control4**  
The [**IDebugControl4**](https://msdn.microsoft.com/library/windows/hardware/ff550508) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Data2"></span><span id="m_data2"></span><span id="M_DATA2"></span>**m\_Data2**  
The [**IDebugDataSpaces2**](https://msdn.microsoft.com/library/windows/hardware/ff550528) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Data3"></span><span id="m_data3"></span><span id="M_DATA3"></span>**m\_Data3**  
The [**IDebugDataSpaces3**](https://msdn.microsoft.com/library/windows/hardware/ff550528) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Data4"></span><span id="m_data4"></span><span id="M_DATA4"></span>**m\_Data4**  
The [IDebugDataSpaces4](https://msdn.microsoft.com/library/windows/hardware/ff550528) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Registers2"></span><span id="m_registers2"></span><span id="M_REGISTERS2"></span>**m\_Registers2**  
The [**IDebugRegisters2**](https://msdn.microsoft.com/library/windows/hardware/ff550825) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Symbols2"></span><span id="m_symbols2"></span><span id="M_SYMBOLS2"></span>**m\_Symbols2**  
The [**IDebugSymbols2**](https://msdn.microsoft.com/library/windows/hardware/ff550856) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_Symbols3"></span><span id="m_symbols3"></span><span id="M_SYMBOLS3"></span>**m\_Symbols3**  
The [**IDebugSymbols3**](https://msdn.microsoft.com/library/windows/hardware/ff550856) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_System2"></span><span id="m_system2"></span><span id="M_SYSTEM2"></span>**m\_System2**  
The [**IDebugSystemObjects2**](https://msdn.microsoft.com/library/windows/hardware/ff550875) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_System3"></span><span id="m_system3"></span><span id="M_SYSTEM3"></span>**m\_System3**  
The [**IDebugSystemObjects3**](https://msdn.microsoft.com/library/windows/hardware/ff550875) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_System4"></span><span id="m_system4"></span><span id="M_SYSTEM4"></span>**m\_System4**  
The [**IDebugSystemObjects4**](https://msdn.microsoft.com/library/windows/hardware/ff550875) interface pointer for the client object that can be used by the extension library. It is valid during the invocation of externally-called extension methods-for example, the execution of an extension command, a call to [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) and **ExtProvideValueMethod**. This interface might not be available in all versions of the debugger engine.

<span id="m_PtrSize"></span><span id="m_ptrsize"></span><span id="M_PTRSIZE"></span>**m\_PtrSize**  
The size of a pointer on the current target. If the target uses 32-bit pointers, **m\_PtrSize** is 4. If the target uses 64-bit pointers, **m\_PtrSize** is 8.

<span id="m_AppendBuffer"></span><span id="m_appendbuffer"></span><span id="M_APPENDBUFFER"></span>**m\_AppendBuffer**  
A character buffer used to return strings from the extension library to the engine. The size of this buffer is **m\_AppendBufferChars**. The methods **AppendBufferString**, **AppendStringVa**, and **AppendString** can be used to write strings to this buffer.

<span id="m_AppendBufferChars"></span><span id="m_appendbufferchars"></span><span id="M_APPENDBUFFERCHARS"></span>**m\_AppendBufferChars**  
The size, in characters, of the buffer **m\_AppendBuffer**.









