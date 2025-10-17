"""
GUI for Key Mapper application
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from key_mapper import KeyMapper


class KeyMapperGUI:
    """GUI for the Key Mapper application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Key Mapper - Map Keys to Applications")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize key mapper
        self.mapper = KeyMapper()
        
        # Set up UI
        self.setup_ui()
        
        # Update UI with current mappings
        self.refresh_mappings()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def setup_ui(self):
        """Set up the user interface"""
        
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Keyboard to Application Mapper", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=10, sticky=tk.W)
        
        # Control buttons frame
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E))
        
        self.start_button = ttk.Button(control_frame, text="Start Mapping", 
                                      command=self.start_mapping, width=15)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(control_frame, text="Stop Mapping", 
                                     command=self.stop_mapping, width=15, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5)
        
        self.restore_button = ttk.Button(control_frame, text="Restore Original", 
                                        command=self.restore_original, width=15)
        self.restore_button.grid(row=0, column=2, padx=5)
        
        self.status_label = ttk.Label(control_frame, text="Status: Stopped", 
                                     foreground="red")
        self.status_label.grid(row=0, column=3, padx=20)
        
        # Add mapping frame
        add_frame = ttk.LabelFrame(main_frame, text="Add New Mapping", padding="10")
        add_frame.grid(row=2, column=0, pady=10, sticky=(tk.W, tk.E))
        add_frame.columnconfigure(1, weight=1)
        
        ttk.Label(add_frame, text="Key Combination:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.key_entry = ttk.Entry(add_frame, width=30)
        self.key_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Label(add_frame, text="(e.g., ctrl+shift+a)").grid(row=0, column=2, sticky=tk.W)
        
        ttk.Label(add_frame, text="Application Path:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.app_entry = ttk.Entry(add_frame, width=50)
        self.app_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        ttk.Button(add_frame, text="Browse...", command=self.browse_app).grid(row=1, column=2, padx=5)
        
        ttk.Button(add_frame, text="Add Mapping", command=self.add_mapping).grid(row=2, column=1, pady=10)
        
        # Mappings list frame
        list_frame = ttk.LabelFrame(main_frame, text="Current Mappings", padding="10")
        list_frame.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)
        
        # Treeview for mappings
        columns = ('Key Combination', 'Application Path')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)
        
        self.tree.heading('Key Combination', text='Key Combination')
        self.tree.heading('Application Path', text='Application Path')
        
        self.tree.column('Key Combination', width=200)
        self.tree.column('Application Path', width=500)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Delete button
        delete_frame = ttk.Frame(list_frame)
        delete_frame.grid(row=1, column=0, pady=10)
        
        ttk.Button(delete_frame, text="Delete Selected", 
                  command=self.delete_mapping).grid(row=0, column=0, padx=5)
        ttk.Button(delete_frame, text="Refresh", 
                  command=self.refresh_mappings).grid(row=0, column=1, padx=5)
        
        # Instructions
        instructions = ("Instructions:\n"
                       "1. Add key combinations (e.g., ctrl+shift+a, alt+f1) and application paths\n"
                       "2. Click 'Start Mapping' to activate key mappings\n"
                       "3. Press your key combinations to launch applications\n"
                       "4. Click 'Restore Original' to remove all mappings")
        
        info_label = ttk.Label(main_frame, text=instructions, justify=tk.LEFT, 
                              foreground="blue", font=('Arial', 9))
        info_label.grid(row=4, column=0, pady=10, sticky=tk.W)
        
    def browse_app(self):
        """Browse for an application"""
        filename = filedialog.askopenfilename(
            title="Select Application",
            filetypes=(("Executable files", "*.exe"), 
                      ("Shortcuts", "*.lnk"),
                      ("All files", "*.*"))
        )
        if filename:
            self.app_entry.delete(0, tk.END)
            self.app_entry.insert(0, filename)
            
    def add_mapping(self):
        """Add a new mapping"""
        key_combo = self.key_entry.get().strip()
        app_path = self.app_entry.get().strip()
        
        if not key_combo or not app_path:
            messagebox.showerror("Error", "Please enter both key combination and application path")
            return
            
        if self.mapper.add_mapping(key_combo, app_path):
            self.mapper.save_mappings()
            self.refresh_mappings()
            self.key_entry.delete(0, tk.END)
            self.app_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Mapping added: {key_combo} -> {app_path}")
            
            # Restart mapping if it was active
            if self.mapper.is_mapping_active():
                self.mapper.stop_mapping()
                self.mapper.start_mapping()
        else:
            messagebox.showerror("Error", "Failed to add mapping. Check that the application path exists.")
            
    def delete_mapping(self):
        """Delete selected mapping"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a mapping to delete")
            return
            
        item = self.tree.item(selected[0])
        key_combo = item['values'][0]
        
        if messagebox.askyesno("Confirm", f"Delete mapping for '{key_combo}'?"):
            if self.mapper.remove_mapping(key_combo):
                self.mapper.save_mappings()
                self.refresh_mappings()
                
                # Restart mapping if it was active
                if self.mapper.is_mapping_active():
                    self.mapper.stop_mapping()
                    self.mapper.start_mapping()
                    
                messagebox.showinfo("Success", "Mapping deleted")
            else:
                messagebox.showerror("Error", "Failed to delete mapping")
                
    def start_mapping(self):
        """Start key mapping"""
        if not self.mapper.get_all_mappings():
            messagebox.showwarning("Warning", "No mappings defined. Add some mappings first.")
            return
            
        if self.mapper.start_mapping():
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Active", foreground="green")
            messagebox.showinfo("Success", "Key mapping started successfully!")
        else:
            messagebox.showerror("Error", "Failed to start key mapping")
            
    def stop_mapping(self):
        """Stop key mapping"""
        if self.mapper.stop_mapping():
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="Status: Stopped", foreground="red")
            messagebox.showinfo("Success", "Key mapping stopped")
        else:
            messagebox.showerror("Error", "Failed to stop key mapping")
            
    def restore_original(self):
        """Restore original key mappings"""
        if messagebox.askyesno("Confirm", 
                              "This will remove all custom mappings. Are you sure?"):
            if self.mapper.restore_original():
                self.refresh_mappings()
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.status_label.config(text="Status: Stopped", foreground="red")
                messagebox.showinfo("Success", "All mappings restored to original")
            else:
                messagebox.showerror("Error", "Failed to restore mappings")
                
    def refresh_mappings(self):
        """Refresh the mappings display"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Add current mappings
        mappings = self.mapper.get_all_mappings()
        for key_combo, app_path in sorted(mappings.items()):
            self.tree.insert('', tk.END, values=(key_combo, app_path))
            
    def on_closing(self):
        """Handle window close event"""
        if self.mapper.is_mapping_active():
            self.mapper.stop_mapping()
        self.root.destroy()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = KeyMapperGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
