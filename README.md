# Pose Label Converter
 Convert pose labels into other sturctures.</br>
 **Supports CSV formats to [MPII](http://human-pose.mpi-inf.mpg.de/) format only for now**

## Requirements
 Vanilla Python will do.

## Getting started

### 1. Clone the Repository

 ```
 git clone https://github.com/bigbreadguy/pose-label-converter.git
 ```

### 2. Create "input" Folder under the Project Directory
 And align target labels each into its own directory seperately.</br>
 </br>
 **Example**
 ```
 ├── pose-label-converter/
 │   ...project files
 ├── input/
 │   ├── inputA/
 │       ├── 0000.csv
 │       │ ...label files (supports .txt in CSV format also)
 │   ├── inputB/
 │       ├── ...label files
 │   ├── ...other label directories
 │
 ```
 ### 3. Run the Script
 ```
 python csv2mpii.py
 ```
