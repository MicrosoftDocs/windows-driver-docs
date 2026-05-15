---
title: Use BinSkim to check binaries
description: This article describes how  driver developers can use BinSkim to examine binary files to identify coding and building practices that can potentially render the binary vulnerable.
ms.date: 12/09/2024
ms.topic: how-to
---

# Use BinSkim to examine binary files to identify  vulnerabilities

Use BinSkim to examine binary files to identify coding and building practices that can potentially render the binary vulnerable. It can be used to check binaries that are getting ready to ship, to help to validate that nothing went wrong in the build chain.

BinSkim checks for:

- Use of outdated compiler tool sets - Binaries should be compiled against the most recent compiler tool sets wherever possible to maximize the use of current compiler-level and OS-provided security mitigations.
- Insecure compilation settings - Binaries should be compiled with the most secure settings possible to enable OS-provided security mitigations, maximize compiler errors and actionable warnings reporting, among other things.
- Signing issues - Signed binaries should be signed with cryptographically-strong algorithms.

BinSkim is an open source tool and generates output files that use the Static Analysis Results Interchange Format ([SARIF](https://github.com/oasis-tcs/sarif-spec)) format. BinSkim replaces the former [BinScope](https://www.microsoft.com/security/blog/2014/11/20/new-binscope-released/) tool.

For more information about BinSkim, see the [BinSkim User Guide](https://github.com/microsoft/binskim/blob/master/docs/UserGuide.md).

## Install and run BinSkim

Follow these steps to validate that the security compile options are properly configured in the code that you are shipping.

1. Download and install the cross platform [.NET Core SDK](https://dotnet.microsoft.com/download).

2. Confirm Visual Studio is installed. For information on downloading and installing Visual Studio see [Install Visual Studio](/visualstudio/install/install-visual-studio).

3. There are a number of options to download BinSkim, such as a NuGet package. In this example we will use the git clone option to download from here: <https://github.com/microsoft/binskim> and install it on a 64 bit Windows PC.

4. Open a Visual Studio Developer Command Prompt window and create a directory, for example `C:\binskim-master`.

   ```console
   C:\> Md \binskim-master
   ```

5. Move to that directory that you just created.

   ```console
   C:\> Cd \binskim-master
   ```

6. Use the git clone command to download all of the needed files.

   ```console
   C:\binskim-master> git clone --recurse-submodules https://github.com/microsoft/binskim.git
   ```

7. Move to the new `binskim` dirctory that the clone command created.

   ```console
   C:\> Cd \binskim-master\binskim
   ```

8. Run **BuildAndTest.cmd** to ensure that release build succeeds, and that all tests pass.

   ```console
   C:\binskim-master\binskim> BuildAndTest.cmd

   Welcome to .NET Core 3.1!
   ---------------------
   SDK Version: 3.1.101

   ...

   C:\binskim-master\binskim\bld\bin\AnyCPU_Release\Publish\netcoreapp2.0\win-x64\BinSkim.Sdk.dll
   1 File(s) copied
   C:\binskim-master\binskim\bld\bin\AnyCPU_Release\Publish\netcoreapp2.0\linux-x64\BinSkim.Sdk.dll
   1 File(s) copied

   ...

   ```

9. The build process creates a set of directories with the BinSkim executables. Move to the win-x64 build output directory.

   ```console
   C:\binskim-master\binskim> Cd \binskim-master\bld\bin\AnyCPU_Release\Publish\netcoreapp2.0\win-x64>
   ```

10. Display help for the analyze option.

   ```console
   C:\binskim-master\binskim\bld\bin\AnyCPU_Release\Publish\netcoreapp2.0\win-x64> BinSkim help analyze

   BinSkim PE/MSIL Analysis Driver 1.6.0.0

   --sympath                      Symbols path value, e.g., SRV*http://msdl.microsoft.com/download/symbols or Cache*d:\symbols;Srv*http://symweb. See
                                 https://learn.microsoft.com/windows-hardware/drivers/debugger/advanced-symsrv-use for syntax information. Note that BinSkim will clear the
                                 _NT_SYMBOL_PATH environment variable at runtime. Use this argument for symbol information instead.

   --local-symbol-directories     A set of semicolon-delimited local directory paths that will be examined when attempting to locate PDBs.

   -o, --output                   File path to which analysis output will be written.

   --verbose                      Emit verbose output. The resulting comprehensive report is designed to provide appropriate evidence for compliance scenarios.

   ...
  
   ```

### Setting the symbol path for BinSkim

If you are building all the code you are analyzing on the same machine you are running BinSkim on, you typically don't need to set the symbol path. This is because your symbol files are available on the local box where you compiled. If you are using a more complex build system, or redirecting your symbols to different location (not alongside the compiled binary), use `--local-symbol-directories` to add these locations to the symbol file search.
If your code references a compiled binary that is not part of your code, the Window debugger sympath can be used to retrieve symbols in order to verify the security of these code dependencies. If you find an issue in these dependencies, you may not be able to fix them. But it can be useful to be aware of any possible security risk you are accepting by taking on those dependencies.

> [!TIP]
>When adding a symbol path (that references a networked symbol server), add a local cache location to specify a local path to cache the symbols. Not doing this can greatly compromise the performance of BinSkim. The following example, specifies a local cache at d:\symbols.
`--sympath Cache*d:\symbols;Srv*http://symweb`
For more information about sympath, see [Symbol path for Windows debuggers](../debugger/symbol-path.md).

1. Execute the following command to analyze a compiled driver binary. Update the target path to point to your complied driver .sys file.

   ```console
   C:\binskim-master\binskim\bld\bin\AnyCPU_Release\Publish\netcoreapp2.0\win-x64> BinSkim analyze "C:\Samples\KMDF_Echo_Driver\echo.sys"
   ```

2. For additional information, add the verbose option like this.

   ```console
   C:\binskim-master\binskim\bld\bin\AnyCPU_Release\Publish\netcoreapp2.0\win-x64> BinSkim analyze "C:\Samples\KMDF_Echo_Driver\osrusbfx2.sys" --verbose
   ```

   > [!NOTE]
   >The --verbose option will produce explicit pass/fail results for every check. If you do not provide verbose, you will only see the defects that BinSkim detects. The --verbose option is typically not recommended for actual automation systems due to the increased size of log files and because it makes it more difficult to pick up individual failures when they occur, as they will be embedded in the midst of a large number of 'pass' results.

3. Review the command output to look for possible issues. This example output shows three tests that passed. Additional information on the rules, such as BA2002 is available in the [BinSkim User Guide](https://github.com/microsoft/binskim/blob/master/docs/UserGuide.md).

   ```console
   Analyzing...
   Analyzing 'osrusbfx2.sys'...
   ...

   C:\Samples\KMDF_Echo_Driver\osrusbfx2.sys\Debug\osrusbfx2.sys: pass BA2002: 'osrusbfx2.sys' does not incorporate any known vulnerable dependencies, as configured by current policy.
   C:\Samples\KMDF_Echo_Driver\Debug\osrusbfx2.sys: pass BA2005: 'osrusbfx2.sys' is not known to be an obsolete binary that is vulnerable to one or more security problems.
   C:\Samples\KMDF_Echo_Driver\osrusbfx2.sys: pass BA2006: All linked modules of 'osrusbfx2.sys' generated by the Microsoft front-end satisfy configured policy (compiler minimum version 17.0.65501.17013).
   ```

4. This output shows that test BA3001 is not run as the tool indicates that the driver is not an ELF binary.

   ```console
   ...
   C:\Samples\KMDF_Echo_Driver\Debug\osrusbfx2.sys: notapplicable BA3001: 'osrusbfx2.sys' was not evaluated for check 'EnablePositionIndependentExecutable' as the analysis is not relevant based on observed metadata: image is not an ELF binary.
   ```

5. This output shows an error for test BA2007.

   ```console
   ...

   C:\Samples\KMDF_Echo_Driver\Debug\osrusbfx2.sys: error BA2007: 'osrusbfx2.sys' disables compiler warning(s) which are required by policy.
   A compiler warning is typically required if it has a high likelihood of flagging memory corruption, information disclosure, or double-free vulnerabilities.
   To resolve this issue, enable the indicated warning(s) by removing /Wxxxx switches (where xxxx is a warning id indicated here) from your command line, and resolve any warnings subsequently raised during compilation.
   ```

To enable these warnings in Visual Studio, under C/C++ in the property pages for the project, remove the values that you don't wish to exclude in **Disable Specific Warnings**.

:::image type="content" source="images/disable-specific-warnings-dialog.png" alt-text="Screenshot of the dialog box for disabling specific warnings in Visual Studio 2019.":::

The default compile options in Visual Studio for driver projects can disable warnings such as the following. These warnings will be reported by BinSkim.

[C4603 - 'name': macro is not defined or definition is different after precompiled header use](/cpp/error-messages/compiler-warnings/compiler-warning-level-1-c4603)

[C4627 - 'description': skipped when looking for precompiled header use](/cpp/error-messages/compiler-warnings/compiler-warning-level-1-c4627)

[C4986 - 'declaration': exception specification does not match previous declaration](/cpp/error-messages/compiler-warnings/compiler-warning-c4986)

For more information about the compiler warnings, see [Compiler Warnings by compiler version](/cpp/error-messages/compiler-warnings/compiler-warnings-by-compiler-version).


### See Also

[Driver security checklist](driver-security-checklist.md)
