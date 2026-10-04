import tkinter as tk
from tkinter import ttk, messagebox


class ContactBook:

    def __init__(self, root):

        self.root = root
        self.root.title("CONTACT BOOK | Professional Contact Manager")
        self.root.geometry("1200x720")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#F4F6FA")

        # ---------------------------------------
        # COLORS
        # ---------------------------------------

        self.dark = "#1E293B"
        self.sidebar_color = "#0F172A"
        self.primary = "#2563EB"
        self.primary_dark = "#1D4ED8"
        self.green = "#10B981"
        self.red = "#EF4444"
        self.orange = "#F59E0B"
        self.light_bg = "#F4F6FA"
        self.white = "#FFFFFF"
        self.text_dark = "#1E293B"
        self.text_gray = "#64748B"

        # ---------------------------------------
        # CONTACT DATA
        # ---------------------------------------

        self.contacts = []
        self.selected_index = None

        # ---------------------------------------
        # MAIN CONTAINER
        # ---------------------------------------

        self.main_frame = tk.Frame(
            self.root,
            bg=self.light_bg
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # CREATE INTERFACE

        self.create_sidebar()
        self.create_main_content()

    # ===========================================
    # SIDEBAR
    # ===========================================

    def create_sidebar(self):

        sidebar = tk.Frame(
            self.main_frame,
            bg=self.sidebar_color,
            width=260
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        # LOGO

        logo_frame = tk.Frame(
            sidebar,
            bg=self.sidebar_color
        )

        logo_frame.pack(
            pady=(40, 10)
        )

        logo = tk.Label(
            logo_frame,
            text="CB",
            font=("Arial", 24, "bold"),
            bg=self.primary,
            fg="white",
            width=4,
            height=2
        )

        logo.pack()

        # APP NAME

        tk.Label(
            sidebar,
            text="CONTACT BOOK",
            font=("Arial", 20, "bold"),
            bg=self.sidebar_color,
            fg="white"
        ).pack(
            pady=(15, 3)
        )

        tk.Label(
            sidebar,
            text="Manage your connections",
            font=("Arial", 10),
            bg=self.sidebar_color,
            fg="#94A3B8"
        ).pack(
            pady=(0, 45)
        )

        # MENU TITLE

        tk.Label(
            sidebar,
            text="NAVIGATION",
            font=("Arial", 9, "bold"),
            bg=self.sidebar_color,
            fg="#64748B"
        ).pack(
            anchor="w",
            padx=30,
            pady=(0, 10)
        )

        # MENU BUTTONS

        self.create_menu_button(
            sidebar,
            "DASHBOARD",
            self.primary
        )

        self.create_menu_button(
            sidebar,
            "ALL CONTACTS",
            self.sidebar_color
        )

        self.create_menu_button(
            sidebar,
            "ADD CONTACT",
            self.sidebar_color
        )

        # BOTTOM INFO

        info_frame = tk.Frame(
            sidebar,
            bg="#172033"
        )

        info_frame.pack(
            side="bottom",
            fill="x",
            padx=20,
            pady=25
        )

        tk.Label(
            info_frame,
            text="YOUR DIGITAL DIRECTORY",
            font=("Arial", 8, "bold"),
            bg="#172033",
            fg="#60A5FA"
        ).pack(
            pady=(15, 8)
        )

        tk.Label(
            info_frame,
            text="Organize, search and manage\nall your important contacts.",
            font=("Arial", 9),
            bg="#172033",
            fg="white",
            justify="center"
        ).pack(
            pady=(0, 15)
        )

    # ===========================================
    # MENU BUTTON
    # ===========================================

    def create_menu_button(self, parent, text, color):

        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 10, "bold"),
            bg=color,
            fg="white",
            activebackground=self.primary,
            activeforeground="white",
            bd=0,
            relief="flat",
            anchor="w",
            padx=30,
            pady=13,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=15,
            pady=4
        )

    # ===========================================
    # MAIN CONTENT
    # ===========================================

    def create_main_content(self):

        content = tk.Frame(
            self.main_frame,
            bg=self.light_bg
        )

        content.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ---------------------------------------
        # HEADER
        # ---------------------------------------

        header = tk.Frame(
            content,
            bg=self.light_bg
        )

        header.pack(
            fill="x",
            padx=35,
            pady=(25, 15)
        )

        tk.Label(
            header,
            text="Contact Dashboard",
            font=("Arial", 26, "bold"),
            bg=self.light_bg,
            fg=self.text_dark
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text="Manage your personal and professional contacts efficiently.",
            font=("Arial", 11),
            bg=self.light_bg,
            fg=self.text_gray
        ).pack(
            anchor="w",
            pady=5
        )

        # ---------------------------------------
        # STATISTICS
        # ---------------------------------------

        stats_frame = tk.Frame(
            content,
            bg=self.light_bg
        )

        stats_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.total_contacts_label = self.create_stat_card(
            stats_frame,
            "TOTAL CONTACTS",
            "0",
            self.primary
        )

        self.email_contacts_label = self.create_stat_card(
            stats_frame,
            "WITH EMAIL",
            "0",
            self.green
        )

        self.phone_contacts_label = self.create_stat_card(
            stats_frame,
            "PHONE RECORDS",
            "0",
            self.orange
        )

        # ---------------------------------------
        # MAIN WORK AREA
        # ---------------------------------------

        work_area = tk.Frame(
            content,
            bg=self.light_bg
        )

        work_area.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=15
        )

        # LEFT SIDE FORM

        self.create_contact_form(work_area)

        # RIGHT SIDE CONTACT LIST

        self.create_contact_list(work_area)

    # ===========================================
    # STATISTICS CARD
    # ===========================================

    def create_stat_card(self, parent, title, number, color):

        card = tk.Frame(
            parent,
            bg=self.white,
            height=100
        )

        card.pack(
            side="left",
            fill="x",
            expand=True,
            padx=7
        )

        card.pack_propagate(False)

        color_bar = tk.Frame(
            card,
            bg=color,
            width=6
        )

        color_bar.pack(
            side="left",
            fill="y"
        )

        number_label = tk.Label(
            card,
            text=number,
            font=("Arial", 24, "bold"),
            bg=self.white,
            fg=self.text_dark
        )

        number_label.place(
            x=30,
            y=18
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 9, "bold"),
            bg=self.white,
            fg=self.text_gray
        ).place(
            x=30,
            y=60
        )

        return number_label

    # ===========================================
    # CONTACT FORM
    # ===========================================

    def create_contact_form(self, parent):

        form_card = tk.Frame(
            parent,
            bg=self.white,
            width=340
        )

        form_card.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        form_card.pack_propagate(False)

        # TITLE

        tk.Label(
            form_card,
            text="Contact Details",
            font=("Arial", 17, "bold"),
            bg=self.white,
            fg=self.text_dark
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 5)
        )

        tk.Label(
            form_card,
            text="Enter the information below.",
            font=("Arial", 9),
            bg=self.white,
            fg=self.text_gray
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 20)
        )

        # NAME

        self.create_form_label(form_card, "FULL NAME")

        self.name_entry = self.create_entry(form_card)

        # PHONE

        self.create_form_label(form_card, "PHONE NUMBER")

        self.phone_entry = self.create_entry(form_card)

        # EMAIL

        self.create_form_label(form_card, "EMAIL ADDRESS")

        self.email_entry = self.create_entry(form_card)

        # ADDRESS

        self.create_form_label(form_card, "ADDRESS")

        self.address_entry = self.create_entry(form_card)

        # BUTTONS

        button_frame = tk.Frame(
            form_card,
            bg=self.white
        )

        button_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        add_button = tk.Button(
            button_frame,
            text="ADD CONTACT",
            font=("Arial", 10, "bold"),
            bg=self.primary,
            fg="white",
            bd=0,
            pady=11,
            cursor="hand2",
            command=self.add_contact
        )

        add_button.pack(
            fill="x",
            pady=4
        )

        update_button = tk.Button(
            button_frame,
            text="UPDATE CONTACT",
            font=("Arial", 10, "bold"),
            bg=self.green,
            fg="white",
            bd=0,
            pady=11,
            cursor="hand2",
            command=self.update_contact
        )

        update_button.pack(
            fill="x",
            pady=4
        )

        clear_button = tk.Button(
            button_frame,
            text="CLEAR FORM",
            font=("Arial", 10, "bold"),
            bg="#E2E8F0",
            fg=self.text_dark,
            bd=0,
            pady=11,
            cursor="hand2",
            command=self.clear_form
        )

        clear_button.pack(
            fill="x",
            pady=4
        )

    # ===========================================
    # FORM LABEL
    # ===========================================

    def create_form_label(self, parent, text):

        tk.Label(
            parent,
            text=text,
            font=("Arial", 8, "bold"),
            bg=self.white,
            fg=self.text_gray
        ).pack(
            anchor="w",
            padx=25,
            pady=(8, 4)
        )

    # ===========================================
    # ENTRY FIELD
    # ===========================================

    def create_entry(self, parent):

        entry = tk.Entry(
            parent,
            font=("Arial", 11),
            bg="#F8FAFC",
            fg=self.text_dark,
            relief="solid",
            bd=1
        )

        entry.pack(
            fill="x",
            padx=25,
            ipady=8
        )

        return entry

    # ===========================================
    # CONTACT LIST SECTION
    # ===========================================

    def create_contact_list(self, parent):

        list_card = tk.Frame(
            parent,
            bg=self.white
        )

        list_card.pack(
            side="left",
            fill="both",
            expand=True
        )

        # TITLE AREA

        title_frame = tk.Frame(
            list_card,
            bg=self.white
        )

        title_frame.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        tk.Label(
            title_frame,
            text="All Contacts",
            font=("Arial", 17, "bold"),
            bg=self.white,
            fg=self.text_dark
        ).pack(
            side="left"
        )

        # SEARCH AREA

        search_frame = tk.Frame(
            list_card,
            bg=self.white
        )

        search_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        self.search_var = tk.StringVar()

        self.search_var.trace_add(
            "write",
            lambda *args: self.search_contacts()
        )

        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 11),
            bg="#F8FAFC",
            relief="solid",
            bd=1
        )

        search_entry.pack(
            fill="x",
            ipady=9
        )

        # TABLE FRAME

        table_frame = tk.Frame(
            list_card,
            bg=self.white
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

        # TREEVIEW STYLE

        style = ttk.Style()

        style.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=35
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        # TREEVIEW

        columns = (
            "Name",
            "Phone",
            "Email",
            "Address"
        )

        self.contact_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.contact_table.heading(
            "Name",
            text="NAME"
        )

        self.contact_table.heading(
            "Phone",
            text="PHONE"
        )

        self.contact_table.heading(
            "Email",
            text="EMAIL"
        )

        self.contact_table.heading(
            "Address",
            text="ADDRESS"
        )

        self.contact_table.column(
            "Name",
            width=130
        )

        self.contact_table.column(
            "Phone",
            width=120
        )

        self.contact_table.column(
            "Email",
            width=170
        )

        self.contact_table.column(
            "Address",
            width=180
        )

        # SCROLLBAR

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.contact_table.yview
        )

        self.contact_table.configure(
            yscrollcommand=scrollbar.set
        )

        self.contact_table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # TABLE CLICK EVENT

        self.contact_table.bind(
            "<<TreeviewSelect>>",
            self.select_contact
        )

        # DELETE BUTTON

        delete_button = tk.Button(
            list_card,
            text="DELETE SELECTED CONTACT",
            font=("Arial", 10, "bold"),
            bg=self.red,
            fg="white",
            bd=0,
            pady=11,
            cursor="hand2",
            command=self.delete_contact
        )

        delete_button.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

    # ===========================================
    # ADD CONTACT
    # ===========================================

    def add_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        # VALIDATION

        if name == "" or phone == "":

            messagebox.showwarning(
                "Missing Information",
                "Name and phone number are required."
            )

            return

        # CREATE CONTACT DICTIONARY

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        # ADD TO LIST

        self.contacts.append(contact)

        # UPDATE INTERFACE

        self.refresh_table()
        self.update_statistics()
        self.clear_form()

        messagebox.showinfo(
            "Success",
            "Contact added successfully!"
        )

    # ===========================================
    # REFRESH TABLE
    # ===========================================

    def refresh_table(self):

        # DELETE OLD DATA

        for item in self.contact_table.get_children():

            self.contact_table.delete(item)

        # INSERT CONTACTS

        for index, contact in enumerate(self.contacts):

            self.contact_table.insert(
                "",
                "end",
                iid=index,
                values=(
                    contact["name"],
                    contact["phone"],
                    contact["email"],
                    contact["address"]
                )
            )

    # ===========================================
    # SELECT CONTACT
    # ===========================================

    def select_contact(self, event):

        selected = self.contact_table.focus()

        if selected == "":
            return

        self.selected_index = int(selected)

        contact = self.contacts[self.selected_index]

        # CLEAR OLD DATA

        self.clear_form()

        # INSERT SELECTED DATA

        self.name_entry.insert(
            0,
            contact["name"]
        )

        self.phone_entry.insert(
            0,
            contact["phone"]
        )

        self.email_entry.insert(
            0,
            contact["email"]
        )

        self.address_entry.insert(
            0,
            contact["address"]
        )

    # ===========================================
    # UPDATE CONTACT
    # ===========================================

    def update_contact(self):

        if self.selected_index is None:

            messagebox.showwarning(
                "Select Contact",
                "Please select a contact to update."
            )

            return

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if name == "" or phone == "":

            messagebox.showwarning(
                "Missing Information",
                "Name and phone number are required."
            )

            return

        # UPDATE DATA

        self.contacts[self.selected_index] = {

            "name": name,
            "phone": phone,
            "email": email,
            "address": address

        }

        # UPDATE DISPLAY

        self.refresh_table()
        self.update_statistics()
        self.clear_form()

        self.selected_index = None

        messagebox.showinfo(
            "Success",
            "Contact updated successfully!"
        )

    # ===========================================
    # DELETE CONTACT
    # ===========================================

    def delete_contact(self):

        if self.selected_index is None:

            messagebox.showwarning(
                "Select Contact",
                "Please select a contact to delete."
            )

            return

        confirmation = messagebox.askyesno(
            "Delete Contact",
            "Are you sure you want to delete this contact?"
        )

        if confirmation:

            del self.contacts[self.selected_index]

            self.selected_index = None

            self.refresh_table()
            self.update_statistics()
            self.clear_form()

            messagebox.showinfo(
                "Deleted",
                "Contact deleted successfully!"
            )

    # ===========================================
    # SEARCH CONTACT
    # ===========================================

    def search_contacts(self):

        search_text = self.search_var.get().lower()

        # CLEAR TABLE

        for item in self.contact_table.get_children():

            self.contact_table.delete(item)

        # SEARCH IN CONTACT LIST

        for index, contact in enumerate(self.contacts):

            name = contact["name"].lower()
            phone = contact["phone"].lower()

            if search_text in name or search_text in phone:

                self.contact_table.insert(
                    "",
                    "end",
                    iid=index,
                    values=(
                        contact["name"],
                        contact["phone"],
                        contact["email"],
                        contact["address"]
                    )
                )

    # ===========================================
    # CLEAR FORM
    # ===========================================

    def clear_form(self):

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        self.selected_index = None

    # ===========================================
    # UPDATE STATISTICS
    # ===========================================

    def update_statistics(self):

        total = len(self.contacts)

        email_count = sum(
            1 for contact in self.contacts
            if contact["email"] != ""
        )

        phone_count = sum(
            1 for contact in self.contacts
            if contact["phone"] != ""
        )

        self.total_contacts_label.config(
            text=str(total)
        )

        self.email_contacts_label.config(
            text=str(email_count)
        )

        self.phone_contacts_label.config(
            text=str(phone_count)
        )


# ===============================================
# RUN APPLICATION
# ===============================================

if __name__ == "__main__":

    root = tk.Tk()

    app = ContactBook(root)

    root.mainloop()