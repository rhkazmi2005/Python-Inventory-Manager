# CIS 1348 - Inventory Management System

A comprehensive Python-based inventory management system that processes electronic device inventory data and provides interactive querying capabilities.

## Project Overview

This project consists of two main components:
- **Part 1**: Data processing and inventory file generation
- **Part 2**: Interactive inventory query system using object-oriented programming

## Features

### Part 1 - Data Processing
- Reads and processes inventory data from multiple input files
- Generates comprehensive inventory reports:
  - `FullInventory.txt` - Complete inventory sorted by manufacturer
  - Item-specific inventory files (e.g., `LaptopInventory.txt`, `PhoneInventory.txt`)
  - `PastServiceDateInventory.txt` - Items past their service date
  - `DamagedInventory.txt` - Damaged items sorted by price

### Part 2 - Interactive Query System
- Object-oriented design using Python classes
- Interactive command-line interface
- Smart item matching and recommendation system
- Alternative product suggestions from different manufacturers

## File Structure

### Input Data Files
- `ManufacturerList.txt` - Item IDs, manufacturers, types, and damage status
- `PriceList.txt` - Item IDs and corresponding prices
- `ServiceDatesList.txt` - Item IDs and service dates

### Generated Output Files
- `FullInventory.txt` - Complete inventory sorted alphabetically by manufacturer
- `LaptopInventory.txt` - Laptop-specific inventory
- `PhoneInventory.txt` - Phone-specific inventory
- `TowerInventory.txt` - Tower-specific inventory
- `PastServiceDateInventory.txt` - Items past service date
- `DamagedInventory.txt` - Damaged items sorted by price

### Source Code
- `part1.py` - Data processing and file generation
- `part2.py` - Interactive query system with OOP design

## Installation & Usage

### Prerequisites
- Python 3.x
- No additional dependencies required (pandas is explicitly prohibited)

### Running Part 1
```bash
python part1.py
```
This will process all input files and generate the inventory reports.

### Running Part 2
```bash
python part2.py
```
This will start the interactive query system where you can search for items.

### Example Queries (Part 2)
- "Apple laptop" - Find Apple laptops
- "Samsung phone" - Find Samsung phones
- "Dell tower" - Find Dell towers

## Technical Details

### Part 1 Implementation
- Processes CSV-formatted input files
- Implements custom sorting algorithms (bubble sort)
- Handles date parsing and comparison for service date filtering
- Manages damaged item identification and sorting

### Part 2 Implementation
- Object-oriented design with `Inventory` class
- Case-insensitive search functionality
- Intelligent matching algorithm for manufacturer and item type
- Alternative recommendation system based on price similarity
- Input validation and error handling

## Data Format

### Input Files
All input files use comma-separated values (CSV) format:

**ManufacturerList.txt:**
```
item_id,manufacturer,item_type,damaged_status
```

**PriceList.txt:**
```
item_id,price
```

**ServiceDatesList.txt:**
```
item_id,service_date
```

### Output Files
Generated files maintain consistent CSV format with appropriate sorting and filtering applied.

## Project Requirements

This project was developed for CIS 1348 (Spring 2025) with the following constraints:
- No pandas library usage
- Extensive code commenting required
- Object-oriented programming principles for Part 2
- Custom sorting algorithms (no built-in sort functions)








