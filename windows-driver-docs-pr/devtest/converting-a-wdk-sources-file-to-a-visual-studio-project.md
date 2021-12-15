---
title: Converting a WDK sources file to a Visual Studio project
description: Using Nmake2msBuild to convert WDK source files to a Visual Studio project.
ms.date: 04/20/2017
---

# Converting a WDK sources file to a Visual Studio project


**Note**  The Nmake2MsBuild tool was removed from the WDK starting in Windows 10, version 1511.

 

For most Windows 7 WDK projects that were built using Build.exe, you can use the [Nmake2MsBuild](nmake2msbuild.md) utility, or the automatic conversion process within Visual Studio, to generate a project file (.VcxProj). In most cases, the Visual Studio project file closely maps to the original *sources* file so the project can be built successfully in Visual Studio, or from an MSBuild command. For some build targets, you need to customize the rule-based mapping that the conversion tools uses. This topic describes how the conversion utility works and how you can extend it by creating your own rule mapping.

## <span id="The_Nmake2MsBuild_conversion_process"></span><span id="the_nmake2msbuild_conversion_process"></span><span id="THE_NMAKE2MSBUILD_CONVERSION_PROCESS"></span>The Nmake2MsBuild conversion process


The [Nmake2MsBuild](nmake2msbuild.md) tool performs a rule-based mapping of the contents of a *sources* file to the contents of a Visual Studio C++ project file (.VcxProj). For each build macro that is to be converted, there is a corresponding conversion rule in a properties file (.props) that is consumed by MSBuild and instrumented during build. In the MSBuild environment, properties, items and metadata on those items are consumed by the build system. Each macro in the *sources* file is mapped to either an MSBuild property, item, or item metadata, as specified by the rule. By default, if no rule is present, a macro named A with the value B is converted to Property A with the value B. The initial conversion step involves a mapping of NMake syntax in a *makefile.inc* or *sources* file to MSBuild syntax in an associated property file (.props). Each macro in the NMake file is converted to a property in a properties file (.props). During build time, these properties are evaluated, and the evaluated values of certain properties are then mapped to various other properties, items or metadata, as specified by a conversion rule.

For example, the USER\_C\_FLAGS macro in a*sources* file is used to specify command-line parameters to be passed to the compiler (cl.exe) during the build. In the MSBuild environment, the ClCompile item list contains the source code files that will be compiled. The ClCompile item list is consumed by the compiler in the [CL Task](/visualstudio/msbuild/cl-task). The AdditionalOptions metadata on each item in the list determines the additional flags passed to the compiler (cl.exe). Therefore, the value of the USER\_C\_FLAGS macro should be mapped to the AdditionalOptions item metadata for items of type ClCompile. In the initial conversion step, the USER\_C\_FLAGS macro in a sources file is converted to an MSBuild property, also named USER\_C\_FLAGS in a generated file called *sources.props*. The mapping of the evaluated value of the USER\_C\_FLAGS property to the AdditionalOptions metadata occurs at build time, as shown in the following example:

```
  <!-- Contains rules to map compiler and linker switches -->
  <ItemDefinitionGroup>
    <ClCompile>
      ...
      <AdditionalOptions>%(AdditionalOptions) $(User_C_Flags)</AdditionalOptions>
      ...
    </ClCompile>
  </ItemDefinitionGroup>
```

The mapping shown in the preceding example is from the PostToolsetRules.props file. The example mapping uses an MSBuild ItemDefinitionGroup to specify that $(User\_C\_Flags) should be appended to all items of type ClCompile within the AdditionalOptions metadata. You can find the properties files used in the conversion process in the C:\\Program Files (x86)\\Windows Kits\\8.0\\bin\\conversion directory.

All of the conversion rules are specified using standard MSBuild syntax.

## <span id="Default_conversion_rules_file"></span><span id="default_conversion_rules_file"></span><span id="DEFAULT_CONVERSION_RULES_FILE"></span>Default conversion rules file


The default rules that are used for conversion are specified in the PostToolsetRules.props file. You can find the PostToolsetRules.props file and the other conversion properties files in the C:\\Program Files (x86)\\Windows Kits\\8.0\\bin\\conversion directory. You can use the PostToolsetRules.props file as a reference for creating new rules for the conversion of your projects.

## <span id="Creating_custom_conversion_rules"></span><span id="creating_custom_conversion_rules"></span><span id="CREATING_CUSTOM_CONVERSION_RULES"></span>Creating custom conversion rules


The default rules file, PostToolsetRules.props, is always used during conversion, but you can also create your own custom rules file. A custom rules file provides additional conversion rules for any build macro that may be specific to the build environment under which the project was built previously.

The rules supplied by Microsoft only support conversion of projects that use the macros and targets defined in the Windows 7 WDK. For example, the rules only support those macros and targets that appear in *makefile.new*. The conversion of any projects that leverage functionality added or modified in the previous build environment is not guaranteed to be automatic. As a general rule, a conversion rules file is necessary if an existing project does not build a fresh installation of the Windows 7 WDK without modification of the sources or .inc files associated with the project, or any other files installed by the WDK.

A custom rules file should follow standard MSBuild syntax, as well as the design patterns that the default rules file uses. The default rules should provide sufficient guidelines and examples for developing all but the most complex conversion rules.

The order in which files are imported in a .VcxProj file, and rules instrumented, is critical and should be maintained. It is recommended that you import the user-developed rules file to the project immediately after the Microsoft supplied PostToolsetRules.props:

```
  <Import Project="$(PostToolsetRules)" />
  <!-- Import PostToolsetRules to map nmake properties/macros to msbuild properties/items/metadata -->
```

## <span id="Conversion_tool_limitations"></span><span id="conversion_tool_limitations"></span><span id="CONVERSION_TOOL_LIMITATIONS"></span>Conversion tool limitations


The NMake2MsBuild utility does not support conversion of custom targets or the conversion of some non-build-critical targets such as BinPlace. BinPlace itself is supported in the MSBuild.exe environment, but not the automatic conversion. The NMake2MsBuild utility does not provide the ability to view all settings for converted projects in the Visual Studio property pages.

## <span id="NMake_syntax_and_behavior_not_supported_by_Nmake2Msbuild"></span><span id="nmake_syntax_and_behavior_not_supported_by_nmake2msbuild"></span><span id="NMAKE_SYNTAX_AND_BEHAVIOR_NOT_SUPPORTED_BY_NMAKE2MSBUILD"></span>NMake syntax and behavior not supported by Nmake2Msbuild


-   Expansion of Macro references in Inference rules that define optional directories:

    ```
    INPUT_DIR= c:\MyDirectory
    .FromExt{$(INPUT_DIR)}.ToExt:
         cmd.exe /c echo  something 
    ```

    You d have to change the above to:

    ```
    .FromExt{ c:\MyDirectory}.ToExt:
         cmd.exe /c echo  something 
    ```

-   NMAKE inline files and macro substitutions are not supported.

    NMAKE inline files: See **Creating Inline File Text**

    Macro substitutions: See **Macro Substitution**

    Because inline files and macro substitutions are not supported the following target won t be converted correctly:

    ```
    fsdkmsg.mc : ..\..\wrapper\fsdkmsgbase.src
           copy ..\..\wrapper\fsdkmsgbase.src
        @type <<$(ECHO_RSP)
    $(ECHO_MSG_P) /EP $**
    <<$(BUILD_NOKEEP)
        @$(C_PREPROCESSOR_NAME) @<<$(CL_RSP) /Tc$** > $@
    $(CPPXX: =
    )
    <<$(BUILD_NOKEEP)   
    ```

-   **!Error** statements will not be converted. There s no equivalent in MSBuild that would work outside MSBuild targets as well.
-   Target definitions must match 1:1 with NTTARGETFILE\* macros that invoke the target: The following is not supported:

    ```
    Sources File:
    OBJ_NAME=Something
    NTTARGETFILES=$(_OBJ_DIR)\$(TARGET_DIRECTORY)\$(OBJ_NAME).obj
    Makefile.inc:
    obj\$(TARGET_DIRECTORY)\Something.obj : $(_OBJ_DIR)\$(TARGET_DIRECTORY)\$(Foo).obj
      
    ```

-   Both the target s definition and NTTARGETFILES must match; they both should use $(OBJ\_NAME).obj or *Somename*.obj. $? And $&lt; tokens in Targets are always expanded for all dependents.

    See **Filename Macros** for more information.

-   $? Expands to  All dependents with a later timestamp than the current target.  For converted projects the timestamp is ignored and this evaluates to all dependents. The same holds true for $&lt;

## <span id="Limitations_of_Converted_Projects"></span><span id="limitations_of_converted_projects"></span><span id="LIMITATIONS_OF_CONVERTED_PROJECTS"></span>Limitations of Converted Projects


If the original sources file conditionally compiled a different set of files and you modify the converted project by renaming/removing/adding files in the IDE, then the project will operate only on the updated list of files. It will no longer conditionally compile different files.

Converted projects do not support VS .Filters files.

## <span id="related_topics"></span>Related topics


[Nmake2MsBuild](nmake2msbuild.md)

[Creating a Driver From Existing Source Files](/windows-hardware/drivers)

 

