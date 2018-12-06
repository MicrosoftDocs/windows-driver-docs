---
title: MSBuild primer for WDK developers
description: This section introduces some basic MSBuild terminology to WDK developers, who are familiar with Build.exe and NMake.exe. This section shows the construction of simple MSBuild projects.
ms.assetid: EA223DF3-71FF-442F-B3E8-56C3B57F7B67
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MSBuild primer for WDK developers


This section introduces some basic MSBuild terminology to WDK developers, who are familiar with Build.exe and NMake.exe. This section shows the construction of simple MSBuild projects.

## <span id="Nmake_concepts_relevant_to_MSBuild"></span><span id="nmake_concepts_relevant_to_msbuild"></span><span id="NMAKE_CONCEPTS_RELEVANT_TO_MSBUILD"></span>Nmake concepts relevant to MSBuild


If you have worked with Build.exe and previous versions of the WDK (prior to WDK 8), you are probably familiar with the terminology and concepts that NMake.exe uses.

-   **command** - invokes a command-line tool.
-   **target** - describes a named sequence of commands.
-   **dependency** - describes a targets that depends on other targets.
-   Nmake is invoked on a make file with one or more targets specified. It then runs all dependencies recursively and then the target's commands.
-   Nmake files can include other make files for the robust management of the build structure.
-   Nmake also supports creating named variables that will be substituted for parameters of commands.
-   Nmake also supports automatic variables that are assigned by the Make.exe itself, for example, the name of the current directory or path.
-   A target will never run twice during a single build. Once run, a target is assumed to have completed its work and will not run again, even if a subsequent target in the build depends on it.

## <span id="MSBuild_concepts_"></span><span id="msbuild_concepts_"></span><span id="MSBUILD_CONCEPTS_"></span>MSBuild concepts


-   The main MSBuild file extension for C++ projects is .vcxproj.
-   Commands are now called *tasks*, and they are not simply invocations of command-line processes. Instead, tasks are units of executable code that MSBuild can use to perform atomic build operations. For a complete list of tasks, see [MSBuild Tasks Specific to Visual C++]( http://go.microsoft.com/fwlink/p/?linkid=236121)..
-   MSBuild imports the tasks from their Common Language Runtime (CLR) assemblies with the **UsingTask** element as the following example shows.
    ```
    <UsingTask TaskName="TaskName" AssemblyName="AssemblyName" />
    ```

-   Targets group tasks together in a particular order and allow the build process to be divided into smaller units.
-   A **PropertyGroup** allows properties to be defined using a human-friendly format. The following example shows the **PropertyGroup** format.
    ```
    <PropertyGroup>
      <ProductVersion>9.0.30729</ProductVersion>
    </PropertyGroup>
    ```

-   An **Item** is an object-oriented variant of **Property**. While the property format is name/value, the item format is name/object where object has multiple attributes. **Items** are arrays of objects.
-   **Properties** are referenced with the format **$(project)** while Items are referenced with the format **@(name)**.
-   An **ItemGroup** is a collection of **Items.**
-   An **ItemGroups** is typically a list all of the files that are to be compiled. The collection of files is then passed to a task using the **@(itemname)** notation. See [MSBuild Items](http://go.microsoft.com/fwlink/p/?linkid=236146) for more information about using **Items.**
-   MSBuild has a number of [built-in properties](http://go.microsoft.com/fwlink/p/?linkid=236149) that you can also reference in a project file.
-   For more information about MSBuild and build tasks, see [MSBuild Concepts](http://go.microsoft.com/fwlink/p/?linkid=236157) and [MSBuild Reference](http://go.microsoft.com/fwlink/p/?linkid=236161).

 

 





