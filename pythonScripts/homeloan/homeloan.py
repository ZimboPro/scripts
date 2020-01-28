#!/usr/bin/python3

from tkinter import *

from tkinter import messagebox

from tkinter import simpledialog

from decimal import *


entries = []

class LoanCalculator:

    def __init__(self):

        self.window = Tk()    #Create Window

        self.window.title("Loan Calculator")    



        #Create Labels

        Label(self.window, text = "Annual Interest Rate").grid(row=1,

              column=1, sticky=W)

        Label(self.window, text="Number of Years").grid(row=2,

              column=1,sticky=W)

        Label(self.window, text="Loan Amount").grid(row=3,

              column=1, sticky=W)

        Label(self.window, text="Monthly Payment").grid(row=4,

              column=1, sticky=W)

        Label(self.window, text="Total Payment").grid(row=5,

              column=1, sticky=W)

        Label(self.window, text="Additional Payment").grid(row=6,

              column=1, sticky=W)

        Label(self.window, text="Reinvest Times").grid(row=6,

              column=3, sticky=W)
    
        Label(self.window, text="Total Years").grid(row=3,

              column=3, sticky=W)

        Label(self.window, text="Total Properties").grid(row=4,

              column=3, sticky=W)



        #Create the text widget with a scroll bar

        self.text = Text(self.window)

        self.text.grid(row = 8, column=1, columnspan = 6, sticky=W)

        scrollbar = Scrollbar(self.window)

        scrollbar.config(command=self.text.yview)

        self.text.config(yscrollcommand = scrollbar.set)

        scrollbar.grid(row = 8, column = 7, columnspan = 10, stick = NS)



        #Create Entries

        self.annualInterestRateVar = StringVar()
        self.annualInterestRateVar.set('11')

        Entry(self.window, textvariable = self.annualInterestRateVar,

              justify = RIGHT).grid(row=1, column=2)



        self.numberOfYearsVar = StringVar()
        self.numberOfYearsVar.set('20')

        Entry(self.window, textvariable = self.numberOfYearsVar,

              justify=RIGHT).grid(row=2, column=2)



        self.loanAmountVar = StringVar()
        self.loanAmountVar.set('500000')

        Entry(self.window, textvariable = self.loanAmountVar,

              justify=RIGHT).grid(row=3, column=2)



        self.monthlyPaymentVar = StringVar()

        lblMonthlyPayment = Label(self.window, textvariable =

                            self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)



        self.totalPaymentVar = StringVar()

        lblTotalPayment = Label(self.window, textvariable = self.totalPaymentVar).grid(

                          row=5, column=2, sticky=E)
        self.totalYears = StringVar()

        lblTotalYears = Label(self.window, textvariable = self.totalYears).grid(

                          row=3, column=4, sticky=E)
        self.totalProperties = StringVar()

        lblTotalYears = Label(self.window, textvariable = self.totalProperties).grid(

                          row=4, column=4, sticky=E)

        self.additionalPayment = StringVar()
        self.additionalPayment.set('5000')

        Entry(self.window, textvariable = self.additionalPayment,

              justify = RIGHT).grid(row=6, column=2)

        self.reInvestTimes = StringVar()
        self.reInvestTimes.set('0')

        Entry(self.window, textvariable = self.reInvestTimes,

              justify = RIGHT).grid(row=6, column=4)



        #Create Button callback

        btComputePayment = Button(self.window, text = "Compute Payment", command =   

                                  self.computePayment).grid(row=7, column=1, sticky=E)

        #Added a button to save a loan

        btSaveLoan = Button(self.window, text = "Save Loan to File", command = self.saveLoanFile).grid(

                            row=7,column=2, sticky=E)
    
        btSaveLoan = Button(self.window, text = "Clear File", command = self.clearFile).grid(

                            row=7,column=3, sticky=E)

        

        self.window.mainloop()  #Create an event loop





    def valueCheck(self):

        interest = self.annualInterestRateVar.get()

        years = self.numberOfYearsVar.get()

        loan =  self.loanAmountVar.get()



        try:

            float(interest)

        except ValueError:

            messagebox.showerror("Calculation Error",

             "Please make sure to enter numeric values for interest rate, years, and loan amount")                     

            self.window.destroy()

            LoanCalculator()



        try:

            float(loan)

        except ValueError:

            messagebox.showerror("Calculation Error",

            "Please make sure to enter numeric values for interest rate, years, and loan amount")                     

            self.window.destroy()

            LoanCalculator()



        try:

            int(years)

        except ValueError:

            messagebox.showerror("Calculation Error",

            "Please make sure to enter numeric values for interest rate, years, and loan amount")                     

            self.window.destroy()

            LoanCalculator()





    def computePayment(self):       #Compute Payment

        self.valueCheck()
        self.totalMonths = 0

            

        monthlyPayment = self.getMonthlyPayment(

            float(self.loanAmountVar.get()),

            float(self.annualInterestRateVar.get()) / 1200,

            int(self.numberOfYearsVar.get())) #Error fix

        self.monthlyPaymentVar.set(format(monthlyPayment,"10.2f"))   #Set monthly payment

        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, "10.2f"))      #Set total payment

        times = int(self.reInvestTimes.get())

        self.totalProperties.set('%d'%(times + 1))

        for time in range(0, times + 1):
            self.calcAmortization(float(self.loanAmountVar.get()),

                              float(self.annualInterestRateVar.get()) / 1200,

                              int(self.numberOfYearsVar.get()),

                              float(self.monthlyPaymentVar.get()),

                              float(self.additionalPayment.get()) + time * monthlyPayment,

                              time + 1)



    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):   #Get monthly payment

        monthlyPayment = loanAmount * monthlyInterestRate / (1-1/(1+monthlyInterestRate)**(numberOfYears * 12))

        return monthlyPayment



    def calcAmortization(self, balance, monthlyInterestRate, numberOfYears, monthlyPayment, additionalPayment, investment):

        getcontext().prec = 2

        self.payNum = 1

        global entries

        entries = entries + ['Property %d'%investment]
        for payNum in range(1, numberOfYears * 12 +1):

            interest = monthlyInterestRate * balance

            principal = monthlyPayment - interest

            balance = balance - principal - additionalPayment
            
            if balance <= 0:
                balance = 0

            entries = entries + [str(self.payNum)+ " => %dy %dm"%(self.payNum//12, self.payNum%12) + "\t\t" + "$"+"%.2f" % interest + "\t\t" + "$"+"%.2f" % principal + "\t" + "  $"+"%.2f" % additionalPayment + "\t\t$"+"%.2f" % balance]

            
            if balance == 0:
                break
            self.payNum += 1
        
        self.totalMonths += self.payNum
    
        self.totalYears.set('%d Years %d Months'%(self.totalMonths//12, self.totalMonths%12))


        if investment > 1:
            self.text.delete(1.0, END)
        
        self.text.insert(END, "Amortization Schedule\n")

        self.text.insert(END,"Pmt #\t\t Interest\t\tPrin Pmt\t Adtn Pay\t    Remaining Prin\n")

        for i in entries:

            self.text.insert(END, i + '\n')

            

    def clearFile(self):
        
        global entries

        entries.clear()

        self.text.delete(1.0, END)


    def saveLoanFile(self):

        filename = simpledialog.askstring("Save Schedule To Recipient", "Enter Recipient Name")



        if (filename == ''):

            messagebox.showerror("Input Error",

            "Please make sure to enter the name of the recipient")

            filename = simpledialog.askstring("Save Schedule To Recipient", "Enter Recipient Name")

            

        

        print(filename+ " Loan Document.txt has been saved")

        f = open(filename+" Loan Document.txt", "w+")

        global entries

        f.write("\t\t\tLoan Document For "+filename+"\n")

        f.write("------------------------------------------------------------------\n\n")

        f.write("Loan Amount: "+"$"+str(self.loanAmountVar.get())+

                "\t\t"+"Interes Rate: "+str(self.annualInterestRateVar.get())+"%"+

                "\t"+"Nbr Years: "+str(self.numberOfYearsVar.get())+"\n")

        f.write("Monthly Payment: "+"$"+str(self.monthlyPaymentVar.get())+

                "\t\t"+"Total Payment: "+"$"+str(self.totalPaymentVar.get())+"\n\n")

        f.write("Amortization Schedule\n")    

        f.write("Pmt #"+"\t\t"+" Interest"+"\t"+"Prin Pmt"+"\t"+"Remaining Prin\n")

        f.write("\n".join(map(lambda x: str(x), entries)))

        f.close()

    

LoanCalculator()  #Create GUI
