---
title: Testing display whitepoint
description: This topic provides instructions on how to use the MALT (Microsoft Ambient Light Tool) to test the display whitepoint.
ms.date: 07/08/2021
---

# Testing display whitepoint

This topic provides instructions on how to test display whitepoint by using the MALT (Microsoft Ambient Light Tool) tool.

## Test requirements

1. **Fully-assembled MALT.** [Building a light and color testing tool (MALT)](testing-MALT-building-a-light-testing-tool.md) has instructions on how to build a MALT or make an existing test apparatus MALT compatible.

1. **Fully calibrated MALT.** [Getting started with MALT](testing-MALT-getting-started.md) has instructions on hardware setup and calibration for the MALT.

1. **Windows device equipped with an ambient light sensor.** The MALT (or compatible tool) is designed to test screen brightness. The system under test (SUT) must have adjustable brightness. [SensorExplorer](testing-sensor-explorer.md) can be used to determine sensors recognized by Windows.

1. **Windows device equipped with the Adaptive Color feature.** The MALT (or compatible tool) is designed to test screen color. The system under test (SUT) must have adjustable color.

## Setup instructions

1. **Plug the MALT into a USB port on the SUT.**

1. **Install SensorExplorer on SUT.** See [Testing with SensorExplorer](testing-sensor-explorer.md)

    > [!Note]
    > If you would like to do manual brightness testing, [download MALTUtil](https://github.com/Microsoft/busiotools/tree/master/sensors/Tools/MALT) from GitHub. Tools can also be found in the HLK.

1. **Configure background color and sleep for SUT.**  The configuration script [MALT_SUT_Setup.bat](https://github.com/Microsoft/busiotools/tree/master/sensors/Tools/MALT/Code/Scripts) will properly setup your device for testing. From an elevated command prompt run `MALT_SUT_Setup.bat` and follow the script instructions.

## MALT sensor placement

:::image type="content" source="images/placement.png" alt-text="Diagram showing MALT sensor placement.":::

Here is a list of tips on MALT sensor placement:

- Place the MALT's screen sensors onto the SUT's screen, facing it.
- The MALT ambient sensors must face towards the light source and away from the SUT's screen.
- Do not block the SUT's ALS sensor. The onboard sensor must not be occluded by the MALT or any other obstruction.
- Place the light enclosure over the SUT such that the light aperture is facing upwards. For best results, the screen should be parallel to the light aperture and facing the light aperture.
- No light should be leaking into or out of the bottom of the enclosure. Double check to make sure the sensors are still in place.
- Mount the light source either inside or on top of the light enclosure. If the light source is mounted on top of the light enclosure, the panel should be placed on top of the box on the aperture such that the light will shine down into the enclosure.
- No light should be leaking from the top of the box. You should not be able to see inside the box at all.

See [Integrating Ambient Light Sensors with Computers Running Windows 10 Creators Update](/windows-hardware/design/whitepapers/integrating-ambient-light-sensors-with-computers-running-windows-10-creators-update) for Microsoft's full guidance on integrating light sensors and ambient light response curves.

## Running the display whitepoint test

**Use the SensorExplorer app (recommended)**

1. Open [SensorExplorer](testing-sensor-explorer.md) and select **MALT** on the left-hand side menu bar. Select the correct Vid/Pid in the **Device Selection** pane and then select **Connect to device**.

    :::image type="content" source="images/connectdevice.png" alt-text="Screenshot of the SensorExplorer MALT page.":::

1. Select **Test Display Whitepoint** on the home tab of the MALT screen in SensorExplorer.

    :::image type="content" source="images/MALTDisplayWhitepoint.png" alt-text="Screenshot of SensorExplorer MALT page displaying the test button.":::

1. This test will output ambient whitepoint, mapped whitepoint, and screen whitepoint values to a CSV file. Choose where to save the CSV file.

1. Specify the wait time in seconds between ambient light changes to give you time to change the lighting conditions for the SUT and MALT.

1. Specify the number of times you will change the lighting conditions.

1. Place the MALT on the screen of the SUT, when and where directed.

    :::image type="content" source="images/MALTBox.png" alt-text="Image of the MALT box.":::

1. After the test completes, the output will be automatically saved to a file called *Whitepoint.csv*.

## Open the results file

1. Open the *Whitepoint.csv* file in Microsoft Excel. If you are using a different app, you'll need to adjust these steps.
1. Select **File** > **Export** > **Change file type**. Change the file type to .xlsx and select **Save As**. This will allow you to create and save visualizations of your data.
1. You will see six columns in your document:

    | Ambient Whitepoint X | Ambient Whitepoint Y | Mapped Whitepoint X | Mapped Whitepoint Y | Screen Whitepoint X | Screen Whitepoint Y |
    |----|----|----|----|----|----|
    | The X chromaticity of the whitepoint value read by the MALT's sensor for the environmental lighting condition. | The Y chromaticity of the whitepoint value read by the MALT's sensor for the environmental lighting condition. | The X chromaticity of the whitepoint value set by Windows. This value may be clamped to a certain range. | The Y chromaticity of the whitepoint value set by Windows. This value may be clamped to a certain range. |  The X chromaticity of the whitepoint value read by the MALT's sensor for the screen whitepoint. Ideally this should be the same as the mapped whitepoint. | The Y chromaticity of the whitepoint value read by the MALT's sensor for the screen whitepoint. Ideally this should be the same as the mapped whitepoint. |

1. The number of rows in your document will correspond to the number of times you told the test you would be changing the lighting conditions.

### Visualize the results

These steps may vary if you are using a program other than Microsoft Excel.

1. In your Microsoft Excel .xlsx file, select the two columns with data: "Ambient Whitepoint X" and "Ambient Whitepoint Y".
1. Select **Insert** > **Insert Scatter (X, Y) or Bubble Chart** > **Scatter with straight lines and markers**

    :::image type="content" source="images/whitepointgraphing.png" alt-text="Screenshot of Microsoft Excel showing a scatter plot.":::

1. Repeat steps 1 and 2 for each X and Y set. You should end up with three graphs in your document.

    :::image type="content" source="images/whitepointgraphingthree.png" alt-text="Screenshot of Microsoft Excel showing three scatter plots.":::

1. Combine three graphs into one graph by copying and pasting the graph itself into one of the other graphs. To do this, select one graph to past all of the data into. We will call this the *Main Graph*. Select a secondary graph and press **CTRL+C**, select the *Main Graph* and press **CTRL+V**. Delete the secondary graphs as they are no longer needed. Do not delete the data in the columns. Your final product should appear similar to below.

    :::image type="content" source="images/combinedgraphs.png" alt-text="Screenshot of Microsoft Excel showing combined plots.":::

## Interpret the results

You must manually inspect the results. Consider if the screen result measured by the MALT matches the mapped output of the Adaptive Color Algorithm.
