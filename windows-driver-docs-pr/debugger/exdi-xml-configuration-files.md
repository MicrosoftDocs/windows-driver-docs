---
title: EXDI XML Configuration files
description: Debugging Tools for Windows supports debugging using EXDI. This topic describes how to configure advanced options using the EXDI XML Configuration files.
ms.date: 10/30/2024
ms.localizationpriority: medium
---

# EXDI XML Configuration files

This topic describes how to configure advanced options using the EXDI XML Configuration files. For general information about using the WinDbg user interface to configure EXDI, see [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md). Most common settings are available in the user interface, which is an easier approach then manually editing the EXDI XML Configuration files, described here.

The Extended Debugging Interface (EXDI) is an adaptation layer between a software debugger and a debugging target. The Debugging Tools for Windows supports kernel debugging using EXDI starting with Windows version 22000.

>[!NOTE]
> EXDI is an advanced, specialized form of debugging for specific environments. Using a standard KDNET connection is easier to configure, and is recommended.  To set up network debugging automatically, see **[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)**.

## Configure advanced options using the EXDI configuration XML files

There are two required xml files that are consumed by the EXDI GDB COM server (ExdiGdbSrv.dll).

1. *exdiConfigData.xml* - This file contains the main configuration data that is required by the GDB server client to establish a successfully GDB session with the HW debugger GDB server target, so the GDB server client won’t run if the file location is *not* set by the EXDI_GDBSRV_XML_CONFIG_FILE environment variable.  Each xml tag allows configuring specific set of the GDB server functionality. See below for a list of the attributes you can modify in the XML, and sample XML.

2. *Systemregister.xml* - This file contains a mapping between system registers and the code used to access the registers. This is needed because the access code is not provided by the GDB server in the xml file, and the debugger accesses each system register via the access code. If the file is not set via the environment variable `EXDI_SYSTEM_REGISTERS_MAP_XML_FILE`, then the ExdiGdbSrv.dll will continue working, but the debugger won’t be able to access any system register via rdmsr or wrmsr commands. The list of these registers should be supported by the GDB server hardware debugger (the specific system register name should be present in the list of registers that is sent in the system xml file).

### EXDI UI and the XML configuration files

The EXDI UI in WinDbg uses the XML file parameters and merges in the UI required parameters, such as the IP:Port value. If there is a need to modify the default XML file parameters, launch the WinDbgNext application from the command line with the parameter `PathToSrvCfgFiles=<path to the modified exdiconfigdata.xml file>`. 
  
#### Target architecture

The EXDI UI target architecture field value needs to match the Windows OS running on the target only for GDB server stubs that do not implement the target description XML file describing the Windows OS target architecture. This target.xml file information is sent by the GDB server stub during the GDB-RSP protocol handshaking between the GDB client and GDB server stub. 

Windbg-ExdiGdbSrv can still set the correct target OS architecture even if the user sets an incorrect target architecture field input value in the EXDI UI. The target OS architecture will be taken and configured from the target.xml description file provided by GDB servers that include the target.xml file in the GDB server handshaking. To check the target architecture, use  the effective machine [.effmach](../debuggercmds/-effmach--effective-machine-.md) debugger command.


## GDBServer Tags and attributes

The following table describes the GDBServer tags and attributes defined in the `exdiConfigData.xml` file.

|Parameter                  | Description                                        |
|---------------------------|----------------------------------------------------|
ExdiTargets     | Specifies which specific GDB server target configuration will be used by the ExdiGgbSrv.dll to establish the GDB connection with the GDB server target, since the exdiConfigData.xml file includes all GDB server supported currently by the ExdiGdbSrv.dll (this file MUST be filled before using the ExdiGdbSrv.dll with a particular GDB server).
CurrentTarget   | Specifies the name of the GDB server target (e.g. this attribute value should match with the name value of one of the `<ExdiTarget Name=` tags included by the exdiConfigData.xml file.
ExdiTarget      | this is the start tag for all configuration data that is included by each GDB server target component.
Name            | Specifies the name of the GDB server (e.g. QEMU, BMC-OpenOCD, Trace32, VMWare).
agentNamePacket | This is the name of the GDB client as it is recognized by the GDB server HW debugger. This can be used by the GDB server HW debugger to configure itself for specific GDB clients (e.g. Trace32 GDB server requires the ExdiGdbSrv.dll to send “QMS.windbg” name to identify the windbg-GDB client and then enable customized GDB memory packets only supported for MS GDB server client (exdiGdbSrv.dll).
ExdiGdbServerConfigData | Specifies the ExdiGdbSrv.dll component related configuration parameters.
uuid            | specifies the UUI of the ExdiGdbSrv.dll component.
displayCommPackets | Flag if ‘yes’, then we will display the RSP protocol communication characters in the command log window. If ‘no’, then we display just the request-response pair text.
enableThrowExceptionOnMemoryErrors | This attribute will be checked by the GDB server client when there is a GDB error response packet (E0x) to determine if the client should throw an exception and stop reading memory.
qSupportedPacket | This allows configuring the GDB client to request which xml register architecture file should be sent by the GDB server HW debugger following the xml target description file (basically, the client will inform the GDB server which architectures are supported by the client, currently, the client does support the x64 architecture).
ExdiGdbServerTargetData | Specifies the parameters related to the hardware Target that is debugged by the GdbServer session.
targetArchitecture | String containing the target hardware architecture. Possible values: X86, X64, ARM, ARM64. Currently, the exdiGdbSrv.dll supports only X86 and ARM.
targetFamily    | String containing the target hardware family. Possible values: ProcessorFamilyX86, ProcessorFamilyX64, ProcessorFamilyARM, ProcessorFamilyARM64.
numberOfCores   | Number of processor cores that the target support. This parameter will be validated when we use a multi-Gdbserver session (T32-GdbServer session). The below ‘MultiCoreGdbServerSessions’ attribute should be set to ‘yes’.
EnableSseContext | Flag if ‘yes’, then the ‘g’ context RSP packet will include floating point registers values. This parameter makes sense only for Intel family targets.
heuristicScanSize | this configures the debugger engine fast heuristic algorithm to decrease the scanned memory probe by the specified size, if the attribute value is *not* specified (or “0”), then the debugger engine won’t use the fast heuristic and fall back to the legacy heuristic that scan the entire memory looking for the PE DOS signature. Common scan size values are 0xfffe (best for NT) or 0xffe (for pre-NT Apps).
targetDescriptionFile | specifies if the GDB server sends a target description header file before sending each separate xml file. This field is blank then the GDB server client won’t request the xml architecture system register (e.g. Trace32 GDBs server that does not support sending architecture registers in a separate xml file).
GdbServerConnectionParameters | Specifies GdbServer session parameters. These parameters are used to control the RSP GdbServer session between the ExdiGdbSrv.dll component and GdbServer.
MultiCoreGdbServerSessions | Flag If ‘yes’, then we will have multi-core GdbServer session (the one used by T32-GdbServer Back-End). If ‘no’, then we will communicate only with one instance of the GdbServer.
MaximumGdbServerPacketLength | This is the maximum GdbServer supported length for one packet.
MaximumConnectAttempts | This is the maximum connection attempts. It is used by the ExdiGdbSrv.dll when it tries to establish the RSP connection to the GdbServer.
SendPacketTimeout | This is the RSP send timeout.
ReceivePacketTimeout | This is the RSP receive timeout.
HostNameAndPort | This is the connection string in the format `<hostname/ip address:Port number>`. There can be more than one GdbServer connection string (like T32 multi-core GdbServer session). The number of connection strings should match with the numbers of cores.
ExdiGdbServerMemoryCommands | Specifies various ways of issuing the GDB memory commands, in order to obtain system registers values or read/write access memory at different exception CPU levels (e.g. BMC-OpenOCD provides access to CP15 register via “aarch64 mrs nsec/sec `<access code>`” customized command).
GdbSpecialMemoryCommand  | if “yes”, then the GDB server supports customized memory commands (e.g. system register, this should be set for Trace32 GDB server).
PhysicalMemory  | if “yes”, then the GDB server supports customized commands for reading physical memory (it is set for Trace32 GDB server).
SupervisorMemory | if “yes”, then the GDB server supports customized commands for reading supervisor memory (it is set for Trace32 GDB server).
SpecialMemoryRegister | if “yes”, then the GDB server supports customized commands for reading system registers (it is set for Trace32 GDB server)
SystemRegistersGdbMonitor | if “yes”, then the GDB server supports customized commands via GDB monitor command (it is set for BMC Open-OCD).
SystemRegisterDecoding | if “yes”, then the GDB client accepts decoding the access code before sending the GDB monitor command.
ExdiGdbServerRegisters | Specifies the specific architecture register core set.
Architecture | CPU architecture of the defined registers set.
FeatureNameSupported | This is the name of the system register group as it’s provided by the xml system register description file. It’s needed to identify the system register xml group that is part of the xml file as it’s sent by the GDB server.
SystemRegistersStart | This is to identify the first system register (low register number/order) that is reported as part of the core register set (e.g. on X64, QEMU does not report the x64 system register set as a separated xml target description file, so system regs are part of the core registers).
SystemRegistersEnd | This is to identify the last system register (high register number/order) that that is reported as part of the core register set.
Name | Name of the register.
Order | This is a number that identifies the index in the array of registers. This number will be used by the GDB client and server set/query (`p<number>”/”q<number>`) register packets.
Size | This is the register size in bytes.

## Sample exdiConfigData.xml file

```xml
<ExdiTargets CurrentTarget = "QEMU">
<!-- QEMU SW simulator GDB server configuration -->
    <ExdiTargets CurrentTarget="QEMU">
    <!--  QEMU SW simulator GDB server configuration  -->
    <ExdiTarget Name="QEMU">
    <ExdiGdbServerConfigData agentNamePacket="" uuid="72d4aeda-9723-4972-b89a-679ac79810ef" displayCommPackets="yes" debuggerSessionByCore="no" enableThrowExceptionOnMemoryErrors="yes" qSupportedPacket="qSupported:xmlRegisters=aarch64,i386">
    <ExdiGdbServerTargetData targetArchitecture="ARM64" targetFamily="ProcessorFamilyARM64" numberOfCores="1" EnableSseContext="no" heuristicScanSize="0xfffe" targetDescriptionFile="target.xml"/>
    <GdbServerConnectionParameters MultiCoreGdbServerSessions="no" MaximumGdbServerPacketLength="1024" MaximumConnectAttempts="3" SendPacketTimeout="100" ReceivePacketTimeout="3000">
    <Value HostNameAndPort="LocalHost:1234"/>
    </GdbServerConnectionParameters>
    <ExdiGdbServerMemoryCommands GdbSpecialMemoryCommand="no" PhysicalMemory="no" SupervisorMemory="no" HypervisorMemory="no" SpecialMemoryRegister="no" SystemRegistersGdbMonitor="no" SystemRegisterDecoding="no"> </ExdiGdbServerMemoryCommands>
        <ExdiGdbServerRegisters Architecture = "ARM64" FeatureNameSupported = "sys">
            <Entry Name ="X0"  Order = "0" Size = "8" />
            <Entry Name ="X1"  Order = "1" Size = "8" />
            <Entry Name ="X2"  Order = "2" Size = "8" />
            <Entry Name ="X3"  Order = "3" Size = "8" />
            <Entry Name ="X4"  Order = "4" Size = "8" />
            <Entry Name ="X5"  Order = "5" Size = "8" />
            <Entry Name ="X6"  Order = "6" Size = "8" />
            <Entry Name ="X7"  Order = "7" Size = "8" />
            <Entry Name ="X8"  Order = "8" Size = "8" />
            <Entry Name ="X9"  Order = "9" Size = "8" />
            <Entry Name ="X10" Order = "a"  Size = "8" />
            <Entry Name ="X11" Order = "b"  Size = "8" />
            <Entry Name ="X12" Order = "c"  Size = "8" />
            <Entry Name ="X13" Order = "d"  Size = "8" />
            <Entry Name ="X14" Order = "e"  Size = "8" />
            <Entry Name ="X15" Order = "f"  Size = "8" />
            <Entry Name ="X16" Order = "10" Size = "8" />
            <Entry Name ="X17" Order = "11" Size = "8" />
            <Entry Name ="X18" Order = "12" Size = "8" />
            <Entry Name ="X19" Order = "13" Size = "8" />
            <Entry Name ="X20" Order = "14" Size = "8" />
            <Entry Name ="X21" Order = "15" Size = "8" />
            <Entry Name ="X22" Order = "16" Size = "8" />
            <Entry Name ="X23" Order = "17" Size = "8" />
            <Entry Name ="X24" Order = "18" Size = "8" />
            <Entry Name ="X25" Order = "19" Size = "8" />
            <Entry Name ="X26" Order = "1a" Size = "8" />
            <Entry Name ="X27" Order = "1b" Size = "8" />
            <Entry Name ="X28" Order = "1c" Size = "8" />
            <Entry Name ="fp"  Order = "1d" Size = "8" />
            <Entry Name ="lr"  Order = "1e" Size = "8" />
            <Entry Name ="sp"  Order = "1f" Size = "8" />
            <Entry Name ="pc"  Order = "20" Size = "8" />
            <Entry Name ="cpsr" Order = "21" Size = "8" />
            <Entry Name ="V0" Order = "22" Size = "16" />
            <Entry Name ="V1" Order = "23" Size = "16" />
            <Entry Name ="V2" Order = "24" Size = "16" />
            <Entry Name ="V3" Order = "25" Size = "16" />
            <Entry Name ="V4" Order = "26" Size = "16" />
            <Entry Name ="V5" Order = "27" Size = "16" />
            <Entry Name ="V6" Order = "28" Size = "16" />
            <Entry Name ="V7" Order = "29" Size = "16" />
            <Entry Name ="V8" Order = "2a" Size = "16" />
            <Entry Name ="V9" Order = "2b" Size = "16" />
            <Entry Name ="V10" Order = "2c" Size = "16" />
            <Entry Name ="V11" Order = "2d" Size = "16" />
            <Entry Name ="V12" Order = "2e" Size = "16" />
            <Entry Name ="V13" Order = "2f" Size = "16" />
            <Entry Name ="V14" Order = "30" Size = "16" />
            <Entry Name ="V15" Order = "31" Size = "16" />
            <Entry Name ="V16" Order = "32" Size = "16" />
            <Entry Name ="V17" Order = "33" Size = "16" />
            <Entry Name ="V18" Order = "34" Size = "16" />
            <Entry Name ="V19" Order = "35" Size = "16" />
            <Entry Name ="V20" Order = "36" Size = "16" />
            <Entry Name ="V21" Order = "37" Size = "16" />
            <Entry Name ="V22" Order = "38" Size = "16" />
            <Entry Name ="V23" Order = "39" Size = "16" />
            <Entry Name ="V24" Order = "3a" Size = "16" />
            <Entry Name ="V25" Order = "3b" Size = "16" />
            <Entry Name ="V26" Order = "3c" Size = "16" />
            <Entry Name ="V27" Order = "3d" Size = "16" />
            <Entry Name ="V28" Order = "3e" Size = "16" />
            <Entry Name ="V29" Order = "3f" Size = "16" />
            <Entry Name ="V30" Order = "3f" Size = "16" />
            <Entry Name ="V31" Order = "3f" Size = "16" />
            <Entry Name ="fpsr" Order = "40" Size = "4" />
            <Entry Name ="fpcr" Order = "41" Size = "4" />
        </ExdiGdbServerRegisters>


        <!-- x64 GDB server core resgisters -->
        <ExdiGdbServerRegisters Architecture = "X64" FeatureNameSupported = "sys" SystemRegistersStart = "18" SystemRegistersEnd = "20" >
            <Entry Name ="rax" Order = "0" Size ="8" />
            <Entry Name ="rbx" Order = "1" Size ="8" />
            <Entry Name ="rcx" Order = "2" Size ="8" />
            <Entry Name ="rdx" Order = "3" Size ="8" />
            <Entry Name ="rsi" Order = "4" Size ="8" />
            <Entry Name ="rdi" Order = "5" Size ="8" />
            <Entry Name ="rbp" Order = "6" Size ="8" />
            <Entry Name ="rsp" Order = "7" Size ="8" />
            <Entry Name ="r8"  Order = "8" Size ="8" />
            <Entry Name ="r9"  Order = "9" Size ="8" />
            <Entry Name ="r10" Order = "a" Size ="8" />
            <Entry Name ="r11" Order = "b" Size ="8" />
            <Entry Name ="r12" Order = "c" Size ="8" />
            <Entry Name ="r13" Order = "d" Size ="8" />
            <Entry Name ="r14" Order = "e" Size ="8" />
            <Entry Name ="r15" Order = "f" Size ="8" />
            <Entry Name ="rip" Order = "10" Size ="8" />
            <!-- <flags id="x64_eflags" size="4">
                <field name="" start="22" end="31"/>
                <field name="ID" start="21" end="21"/>
                <field name="VIP" start="20" end="20"/>
                <field name="VIF" start="19" end="19"/>
                <field name="AC" start="18" end="18"/>
                <field name="VM" start="17" end="17"/>
                <field name="RF" start="16" end="16"/>
                <field name="" start="15" end="15"/>
                <field name="NT" start="14" end="14"/>
                <field name="IOPL" start="12" end="13"/>
                <field name="OF" start="11" end="11"/>
                <field name="DF" start="10" end="10"/>
                <field name="IF" start="9" end="9"/>
                <field name="TF" start="8" end="8"/>
                <field name="SF" start="7" end="7"/>
                <field name="ZF" start="6" end="6"/>
                <field name="" start="5" end="5"/>
                <field name="AF" start="4" end="4"/>
                <field name="" start="3" end="3"/>
                <field name="PF" start="2" end="2"/>
                <field name="" start="1" end="1"/>
                <field name="CF" start="0" end="0"/>
            </flags> -->
            <Entry Name ="eflags" Order = "11" Size ="4" />

            <!-- Segment registers -->
            <Entry Name ="cs" Order = "12" Size ="4" />
            <Entry Name ="ss" Order = "13" Size ="4" />
            <Entry Name ="ds" Order = "14" Size ="4" />
            <Entry Name ="es" Order = "15" Size ="4" />
            <Entry Name ="fs" Order = "16" Size ="4" />
            <Entry Name ="gs" Order = "17" Size ="4" />

            <!-- Segment descriptor caches and TLS base MSRs -->
            <!--Entry Name ="cs_base" Order = "18" Size="8"/
            <Entry Name ="ss_base" Order = "18" Size ="8" />
            <Entry Name ="ds_base" Order = "19" Size ="8" />
            <Entry Name ="es_base" Order = "1a" Size ="8" /> -->
            <Entry Name ="fs_base" Order = "18" Size ="8" />
            <Entry Name ="gs_base" Order = "19" Size ="8" />
            <Entry Name ="k_gs_base" Order = "1a" Size ="8" />

            <!-- Control registers -->
            <!-- the cr0 register format fields:
            <flags id="x64_cr0" size="8">
            <field name="PG" start="31" end="31"/>
            <field name="CD" start="30" end="30"/>
            <field name="NW" start="29" end="29"/>
            <field name="AM" start="18" end="18"/>
            <field name="WP" start="16" end="16"/>
            <field name="NE" start="5" end="5"/>
            <field name="ET" start="4" end="4"/>
            <field name="TS" start="3" end="3"/>
            <field name="EM" start="2" end="2"/>
            <field name="MP" start="1" end="1"/>
            <field name="PE" start="0" end="0"/>
            </flags> -->
            <Entry Name ="cr0" Order = "1b" Size ="8" />
            <Entry Name ="cr2" Order = "1c" Size ="8" />

            <!-- the cr3 register format fields:
            <flags id="x64_cr3" size="8">
                <field name="PDBR" start="12" end="63"/>
                <field name="PCID" start="0" end="11"/>
            </flags> -->
            <Entry Name ="cr3" Order = "1d" Size ="8" />

            <!-- the cr4 register format fields:
            <flags id="x64_cr4" size="8">
                <field name="PKE" start="22" end="22"/>
                <field name="SMAP" start="21" end="21"/>
                <field name="SMEP" start="20" end="20"/>
                <field name="OSXSAVE" start="18" end="18"/>
                <field name="PCIDE" start="17" end="17"/>
                <field name="FSGSBASE" start="16" end="16"/>
                <field name="SMXE" start="14" end="14"/>
                <field name="VMXE" start="13" end="13"/>
                <field name="LA57" start="12" end="12"/>
                <field name="UMIP" start="11" end="11"/>
                <field name="OSXMMEXCPT" start="10" end="10"/>
                <field name="OSFXSR" start="9" end="9"/>
                <field name="PCE" start="8" end="8"/>
                <field name="PGE" start="7" end="7"/>
                <field name="MCE" start="6" end="6"/>
                <field name="PAE" start="5" end="5"/>
                <field name="PSE" start="4" end="4"/>
                <field name="DE" start="3" end="3"/>
                <field name="TSD" start="2" end="2"/>
                <field name="PVI" start="1" end="1"/>
                <field name="VME" start="0" end="0"/>
            </flags> -->
            <Entry Name ="cr4" Order = "1e" Size ="8" />
            <Entry Name ="cr8" Order = "1f" Size ="8" />

            <!-- the efer register format fields:
            <flags id="x64_efer" size="8">
            <field name="TCE" start="15" end="15"/>
            <field name="FFXSR" start="14" end="14"/>
            <field name="LMSLE" start="13" end="13"/>
            <field name="SVME" start="12" end="12"/>
            <field name="NXE" start="11" end="11"/>
            <field name="LMA" start="10" end="10"/>
            <field name="LME" start="8" end="8"/>
            <field name="SCE" start="0" end="0"/>
            </flags> -->
            <Entry Name ="efer" Order = "20" Size ="8"/>

            <!-- x87 FPU -->
            <Entry Name ="st0" Order = "21" Size ="10" />
            <Entry Name ="st1" Order = "22" Size ="10" />
            <Entry Name ="st2" Order = "23" Size ="10" />
            <Entry Name ="st3" Order = "24" Size ="10" />
            <Entry Name ="st4" Order = "25" Size ="10" />
            <Entry Name ="st5" Order = "26" Size ="10" />
            <Entry Name ="st6" Order = "27" Size ="10" />
            <Entry Name ="st7" Order = "28" Size ="10" />
            <Entry Name ="fctrl" Order = "29" Size ="4" />
            <Entry Name ="fstat" Order = "2a" Size ="4" />
            <Entry Name ="ftag"  Order = "2b" Size ="4" />
            <Entry Name ="fiseg" Order = "2c" Size ="4" />
            <Entry Name ="fioff" Order = "2d" Size ="4" />
            <Entry Name ="foseg" Order = "2e" Size ="4" />
            <Entry Name ="fooff" Order = "2f" Size ="4" />
            <Entry Name ="fop" Order = "30" Size ="4" />
            <Entry Name ="xmm0" Order = "31" Size ="16"  />
            <Entry Name ="xmm1" Order = "32" Size ="16"  />
            <Entry Name ="xmm2" Order = "33" Size ="16"  />
            <Entry Name ="xmm3" Order = "34" Size ="16"  />
            <Entry Name ="xmm4" Order = "35" Size ="16"  />
            <Entry Name ="xmm5" Order = "36" Size ="16"  />
            <Entry Name ="xmm6" Order = "37" Size ="16"  />
            <Entry Name ="xmm7" Order = "38" Size ="16"  />
            <Entry Name ="xmm8" Order = "39" Size ="16"  />
            <Entry Name ="xmm9" Order = "3a" Size ="16"  />
            <Entry Name ="xmm10" Order = "3b" Size ="16"  />
            <Entry Name ="xmm11" Order = "3c" Size ="16"  />
            <Entry Name ="xmm12" Order = "3d" Size ="16"  />
            <Entry Name ="xmm13" Order = "3e" Size ="16"  />
            <Entry Name ="xmm14" Order = "3f" Size ="16"  />
            <Entry Name ="xmm15" Order = "40" Size ="16"  />
            
            <!-- the mxcsr register format fields:
            <flags id="x64_mxcsr" size="4">
                <field name="IE" start="0" end="0"/>
                <field name="DE" start="1" end="1"/>
                <field name="ZE" start="2" end="2"/>
                <field name="OE" start="3" end="3"/>
                <field name="UE" start="4" end="4"/>
                <field name="PE" start="5" end="5"/>
                <field name="DAZ" start="6" end="6"/>
                <field name="IM" start="7" end="7"/>
                <field name="DM" start="8" end="8"/>
                <field name="ZM" start="9" end="9"/>
                <field name="OM" start="10" end="10"/>
                <field name="UM" start="11" end="11"/>
                <field name="PM" start="12" end="12"/>
                <field name="FZ" start="15" end="15"/>
            </flags> -->
            <Entry Name ="mxcsr" Order = "41" Size ="4" />

        </ExdiGdbServerRegisters>
    </ExdiGdbServerConfigData>
    </ExdiTarget>
    </ExdiTargets>
</ExdiTargets>
```

## Example EXDI PowerShell script

This sample PowerShell script installs EXDI and then launches the debugger. The Start-ExdiDebugger.ps1 script will install ExdiGdbSrv.dll if required, configure the xml settings files, check for running dllhost.exe processes, and launch the debugger to connect to an already running gdb server hardware debugging target.

When using the user interface avalible with WinDBg, the ExdiGdbSrv.dll is already installed, and this script is not relevant. For more information on using the built in user interface, see  [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md).

This is an example of calling the start up script.

```powershell
PS>.\Start-ExdiDebugger.ps1 -ExdiTarget "QEMU" -GdbPort 1234 -Architecture x64
```

You can also specify the built files if necessary.

```powershell
PS>.\Start-ExdiDebugger.ps1 -ExdiTarget "QEMU" -GdbPort 1234 -Architecture x64 -ExdiDropPath "C:\path\to\built\exdi\files"
```

The Start-ExdiDebugger.ps1 has the following settings options.

| Parameter                            | Description                      |
|--------------------------------------|----------------------------------|
ExdiTarget | The type of target to connect to. This corresponds to a specific section in the settings xml file
HostName   | The IP address or hostname of the computer hosting the gdb server session (defaults to "LocalHost")
GdbPort    | The Port that the gdb server is listening on.
Architecture | Architecture of the hardware debugging target (this parameter also implies the ArchitectureFamily parameter in the xml settings file)
ExdiDropPath | Location of the ExdiGdbSrv.dll, exdiConfigData.xml, and systemregisters.xml files. These will only be copied if ExdiGdbSrv.dll is not installed or is installed incorrectly.
ExtraDebuggerArgs | Extra arguments to pass on the debugger command line
PreNTAppDebugging | Changes the value of the heuristicScanSize from 0xfffe (best for NT) to 0xffe (for pre-NT Apps)
DontTryDllHostCleanup | Checking for existing running instances of ExdiGdbSrv.dll in dllhost.exe requires elevation. Providing this switch will allow the script to run without elevation (although the debugger may not function correctly).

To enable packets to be displayed, set the value of *displayCommPackets* to yes. 

```powershell
    [pscustomobject]@{ Path = 'displayCommPackets'                                  ; value = "yes" } 
```

```powershell
.\Start-ExdiDebugger.ps1 -ExdiTarget "QEMU" -GdbPort 1234 -Architecture x64 -ExdiDropPath "C:\path\to\built\exdi\files"
```

See the code comments for more settings options.

```powershell
<#
.Synopsis
    Installs and launches exdi debugger (automating xml file editing)

.Description
    This script will install ExdiGdbSrv.dll if required, configure the xml settings
    files, check for running dllhost.exe processes, and launch the debugger to connect to
    an already running gdb server hardware debugging target.

.Parameter ExdiTarget
    Type of target to connect to. This corresponds to a specific section in the settings xml file

.Parameter HostName
    IP address or hostname of the computer hosting the gdb server session (defaults to "LocalHost")

.Parameter GdbPort
    Port that the gdb server is listening on.

.Parameter Architecture
    Architecture of the hardware debugging target (this parameter also implies the ArchitectureFamily
    parameter in the xml settings file)

.Parameter ExdiDropPath
    Location of the ExdiGdbSrv.dll, exdiConfigData.xml, and systemregisters.xml files. These will
    only be copied if ExdiGdbSrv.dll is not installed or is installed incorrectly.

.Parameter ExtraDebuggerArgs
    Extra arguments to pass on the debugger command line

.Parameter PreNTAppDebugging
    Changes the value of the heuristicScanSize from 0xfffe (best for NT) to 0xffe (for pre-NT Apps)

.Parameter DontTryDllHostCleanup
    Checking for existing running instances of ExdiGdbSrv.dll in dllhost.exe requires elevation.
    Providing this switch will allow the script to run without elevation (although the debugger may not
    function correctly).

.Example
    >---------------- (first run) ------------<
    .\Start-ExdiDebugger.ps1 -ExdiTarget "QEMU" -GdbPort 1234 -Architecture x64 -ExdiDropPath "C:\path\to\built\exdi\files"

.Example
    PS>.\Start-ExdiDebugger.ps1 -ExdiTarget "QEMU" -GdbPort 1234 -Architecture x64
#>

[CmdletBinding()]
param
(
    [ValidateSet("QEMU")]
    [string]
    $ExdiTarget = "QEMU",

    [string]
    $HostName = "LocalHost",

    [Parameter(Mandatory=$true)]
    [Int]
    $GdbPort,

    [Parameter(Mandatory=$true)]
    [string]
    [ValidateSet("x86", "x64", "arm64")]
    $Architecture,

    [string]
    $ExdiDropPath,

    [string]
    $DebuggerPath,

    [string[]]
    $ExtraDebuggerArgs = @(),

    [switch]
    $PreNTAppDebugging,

    [switch]
    $DontTryDllHostCleanup
)

$ErrorActionPreference = "Stop"

#region Functions

Function Test-Admin
{
    ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator")
}

Function Find-PathToWindbgX
{
    $InternalWindbgXPath = "$env:LOCALAPPDATA\DBG\UI\WindbgX.exe"
    $ExternalWindbgXPath = "$env:LOCALAPPDATA\Microsoft\WindowsApps\WinDbgX.exe"

    if (Test-Path $InternalWindbgXPath -PathType Leaf)
    {
        return $InternalWindbgXPath
    }
    elseif (Test-Path $ExternalWindbgXPath -PathType Leaf)
    {
        return $ExternalWindbgXPath
    }
}

Function Test-ParameterValidation
{
    $CommandName = $PSCmdlet.MyInvocation.InvocationName
    $ParameterList = (Get-Command -Name $CommandName).Parameters

    foreach ($Parameter in $ParameterList) {
        Get-Variable -Name $Parameter.Values.Name -ErrorAction SilentlyContinue | Out-String | Write-Verbose
    }

    if (-not $DebuggerPath)
    {
        throw "WindbgX is not installed"
    }
    elseif (-not (Test-Path $DebuggerPath -PathType Leaf))
    {
        throw "DebuggerPath param ($DebuggerPath) does not point to a debugger."
    }

    # Searching for loaded instances of ExdiGdbSrv.dll in dllhost.exe requires elevation
    if (-not $DontTryDllHostCleanup -and
        -not $(Test-Admin))
    {
        throw "Searching for loaded instances of ExdiGdbSrv.dll in dllhost.exe requires elevation. Run with the -DontTryDllHostCleanup parameter to skip this check (debugger session init may fail)."
    }
}

Function Get-ExdiInstallPath
{
    Get-ItemPropertyValue -Path "Registry::HKEY_CLASSES_ROOT\CLSID\{29f9906e-9dbe-4d4b-b0fb-6acf7fb6d014}\InProcServer32" -Name "(default)" -ErrorAction SilentlyContinue
}

Function Test-ExdiServerInstalled
{
    # Check registration of exdi server class
    if ($(Get-ExdiInstallPath) -ne $null -and $(Test-Path "$(Get-ExdiInstallPath)"))
    {
        Write-Verbose "Exdi server is installed. Checking installation..."
        $ExdiInstallDir = [System.IO.Path]::GetDirectoryName($(Get-ExdiInstallPath))
        if (-not (Test-Path $ExdiInstallDir))
        {
            Write-Host "Currently Registered exdi server does not exist. Reinstalling..."
            return $false
        }
        elseif (-not ((Test-Path "$ExdiInstallDir\exdiConfigData.xml") -and (Test-Path "$ExdiInstallDir\systemregisters.xml")))
        {
            Write-Host "Currently Registered exdi server does not have required xml settings files. Reinstalling..."
            return $false
        }
        else
        {
            Write-Verbose "Exdi server is insalled correctly. Skipping installation..."
            return $true
        }
    }
    else
    {
        Write-Host "Exdi server is not installed. Installing..."
        return $false
    }
}

Function Install-ExdiServer
{
    [CmdletBinding()]
    param
    (
        [string] $InstallFrom,
        [string] $InstallTo
    )
    
    if (-not $(Test-Admin))
    {
        throw "Script needs to be run as an Admin to install exdi software."
    }

    New-Item -ItemType Directory $InstallTo -ErrorAction SilentlyContinue | Write-Verbose
    Copy-Item -Path "$InstallFrom\ExdiGdbSrv.dll" -Destination $InstallTo -ErrorAction stop | Write-Verbose
    Copy-Item -Path "$InstallFrom\exdiConfigData.xml" -Destination $InstallTo -ErrorAction stop | Write-Verbose
    Copy-Item -Path "$InstallFrom\systemregisters.xml" -Destination $InstallTo -ErrorAction stop | Write-Verbose
    regsvr32 /s "$InstallTo\ExdiGdbSrv.dll"

    if ($(Get-ExdiInstallPath) -eq $null)
    {
        throw "Unable to install exdi server"
    }
}

Function Edit-ExdiConfigFile
{
    [CmdletBinding()]
    param
    (
        [string] $ExdiFilePath,
        [string] $ExdiTargetType,
        [PSCustomObject[]] $XmlSettingPathValueList
    )
    
    # Edit exdiConfigData.xml
    [xml]$exdiConfigXml = Get-Content "$ExdiFilePath"

    # Set current target
    $exdiConfigXml.ExdiTargets.CurrentTarget = $ExdiTarget

    # set HostNameAndPort
    $ExdiTargetXmlNode = $exdiConfigXml.SelectSingleNode("//ExdiTargets/ExdiTarget[@Name='$ExdiTarget']/ExdiGdbServerConfigData")

    foreach ($XmlSettingPathValue in $XmlSettingPathValueList)
    {
        Write-Verbose "Processing $XmlSettingPathValue"
        if ($XmlSettingPathValue.Value -eq $null)
        {
            continue
        }

        $PathParts = $XmlSettingPathValue.Path.Split(".")
        $curNode = $ExdiTargetXmlNode
        if ($PathParts.Count -gt 1)
        {
            foreach ($PathPart in $PathParts[0..($PathParts.Count-2)])
            {
                Write-Verbose $PathPart
                $curNode = $curNode.($PathPart)
            }
        }
        $curNode.($PathParts[-1]) = $XmlSettingPathValue.Value
    }

    $exdiConfigXml.Save("$ExdiFilePath")
}

Function Stop-ExdiContainingDllHosts
{
    $DllHostPids = Get-Process dllhost | ForEach-Object { $_.Id }
    foreach ($DllHostPid in $DllHostPids)
    {
        $DllHostExdiDlls = Get-Process -Id $DllHostPid -Module | Where-Object { $_.FileName -like "*ExdiGdbSrv.dll" }
        if ($DllHostExdiDlls.Count -ne 0)
        {
            Write-Verbose "Killing dllhost.exe with pid $DllHostPid (Contained instance of ExdiGdbSrv.dll)"
            Stop-Process -Id $DllHostPid -Force
        }
    }
}

#endregion

#region Script

# Apply defaults for $DebuggerPath before Parameter validation
if (-not $DebuggerPath)
{
    $DebuggerPath = Find-PathToWindbgX
}

Test-ParameterValidation

# look clean up dllhost.exe early since it can hold a lock on files which
# need to be overwritten
if (-not $DontTryDllHostCleanup)
{
    Stop-ExdiContainingDllHosts
}

if (-not $(Test-ExdiServerInstalled))
{
    if (-not $ExdiDropPath)
    {
        throw "ExdiServer is not installed and -ExdiDropPath is not valid"
    }

    $ExdiInstallDir = Join-Path -Path "$([System.IO.Path]::GetDirectoryName($DebuggerPath))" -ChildPath "exdi"
    Install-ExdiServer -InstallFrom "$ExdiDropPath" -InstallTo "$ExdiInstallDir"
}

$SystemRegistersFilepath = Join-Path -Path "$([System.IO.Path]::GetDirectoryName($(Get-ExdiInstallPath)))" -ChildPath "systemregisters.xml"
$ExdiConfigFilepath      = Join-Path -Path "$([System.IO.Path]::GetDirectoryName($(Get-ExdiInstallPath)))" -ChildPath "exdiConfigData.xml"

# Calculate implied parameters
$HeuristicScanSize = if ($PreNTAppDebugging) { "0xffe" } else { "0xfffe" }
$ArchitectureFamily = switch($Architecture)
{
    x64   { "ProcessorFamilyx64" }
    x86   { "ProcessorFamilyx86" }
    arm64 { "ProcessorFamilyARM64" }
}

# Path is evaluated relative to the relevant ExdiTarget's ExdiGdbServerConfigData node in the xml schema
$SettingsToChange = @(
    [pscustomobject]@{ Path = 'GdbServerConnectionParameters.Value.HostNameAndPort' ; Value = "${HostName}:$GdbPort" },
    [pscustomobject]@{ Path = 'ExdiGdbServerTargetData.targetArchitecture'          ; Value = "$Architecture" },
    [pscustomobject]@{ Path = 'ExdiGdbServerTargetData.targetFamily'                ; Value = "$ArchitectureFamily" },
    [pscustomobject]@{ Path = 'ExdiGdbServerTargetData.heuristicScanSize'           ; Value = "$HeuristicScanSize" },
    [pscustomobject]@{ Path = 'displayCommPackets'                                  ; value = "no" }
)
Edit-ExdiConfigFile -ExdiFilePath "$ExdiConfigFilepath" -ExdiTargetType "$ExdiTarget" -XmlSettingPathValueList $SettingsToChange

# Set env vars for debugger
[System.Environment]::SetEnvironmentVariable('EXDI_GDBSRV_XML_CONFIG_FILE',"$ExdiConfigFilepath")
[System.Environment]::SetEnvironmentVariable('EXDI_SYSTEM_REGISTERS_MAP_XML_FILE',"$SystemRegistersFilepath")

$DebuggerArgs = @("-v", "-kx exdi:CLSID={29f9906e-9dbe-4d4b-b0fb-6acf7fb6d014},Kd=Guess,DataBreaks=Exdi")
Write-Verbose "DebuggerPath = $DebuggerPath"
Start-Process -FilePath "$DebuggerPath" -ArgumentList ($DebuggerArgs + $ExtraDebuggerArgs)

#endregion
```

## See also

[Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md)

[Setting Up QEMU Kernel-Mode Debugging Using EXDI](setting-up-qemu-kernel-mode-debugging-using-exdi.md)

[.exdicmd (EXDI Command)](../debuggercmds/-exdicmd--exdi-command-.md)

[Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)


