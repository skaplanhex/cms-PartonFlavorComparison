from ROOT import *
#gROOT.SetStyle("Plain")
#SetBatch() makes it so the picture isn't displayed on the screen when saved; this saves lots of time!
gROOT.SetBatch()
gStyle.SetOptStat(11)
c = TCanvas()
c.SetBorderMode(0)
c.SetFillColor(kWhite)
genDict = {'tt_pythia6_plots.root':'pythia6','tt_pythia8_plots.root':'pythia8','tt_sherpa_plots.root':'sherpa','tt_mg_plots.root':'mg','tt_herwig6_pythiastatus_plots.root':'herwig6_pythiastatus','tt_herwig6_herwigstatus_plots.root':'herwig6_herwigstatus'}
binLabelDict = {1:'b',2:'c',3:'d',4:'g',5:"noMatch",6:'s',7:'u'}
numGenDict = {0:'pythia6',1:'pythia8',2:'sherpa',3:'mg',4:'herwig6_pythiastatus',5:'herwig6_herwigstatus'}

bHistos = []
cHistos = []
sHistos = []
noMatchHistos = []
uHistos = []
dHistos = []
gHistos = []
lightHistos = [] #lightHisto = u+d+s+g
flavorHistos = []

bHistosOld = []
cHistosOld = []
sHistosOld = []
noMatchHistosOld = []
uHistosOld = []
dHistosOld = []
gHistosOld = []
lightHistosOld = [] #lightHisto = u+d+s+g
flavorHistosOld = []

c = TCanvas()
counter = 0
for filename in ('oldplotrootfiles/tt_pythia8_plots.root','tt_pythia8_status71_plots_nocuts.root'):
	counter += 1
	f = TFile(filename,"READ")

	histptold = f.Get('analyzerAK5/hPartonFlavorOld_Pt')
	histptnew = f.Get('analyzerAK5/hPartonFlavorNew_Pt')

	histptold.LabelsOption('a','Y')
	histptnew.LabelsOption('a','Y')

	flavHistNew = histptnew.ProjectionY()
	flavHistNew.LabelsOption('a','X') #may not be needed, but I guess it doesn't hurt
	flavHistNew.SetDirectory(0) #don't go out of scope!
	if (counter == 1):
		flavHistNew.SetName("pythia8_oldstatusdef_flavordist")
	elif (counter == 2):
		flavHistNew.SetName("pythia8_status71_flavordist")
	flavHistNew.GetYaxis().SetRangeUser(0,125000)
	flavorHistos.append(flavHistNew)

	flavHistOld = histptold.ProjectionY()
	flavHistOld.LabelsOption('a','X') #may not be needed, but I guess it doesn't hurt
	flavHistOld.SetDirectory(0)
	flavHistOld.GetYaxis().SetRangeUser(0,125000)
	flavorHistosOld.append(flavHistOld)


#pythia 8 old status convention
flavorHistos[0].SetLineColor(kBlack)
flavorHistos[0].SetMarkerColor(kBlack)
flavorHistos[0].SetMarkerStyle(20)

#pythia 8 status==71
flavorHistos[1].SetLineColor(kBlue)
flavorHistos[1].SetMarkerColor(kBlue)
flavorHistos[1].SetMarkerStyle(21)

flavorHistos[0].SetTitle("Jet Parton Flavor")
flavorHistos[0].GetXaxis().SetTitle("Jet Flavor")
flavorHistos[0].GetYaxis().SetTitle("Number Of Jets / Flavor")
flavorHistos[0].GetYaxis().SetTitleOffset(1.4)
flavorHistos[0].Draw()
flavorHistos[0].Draw("sameP0")
flavorHistos[1].Draw("same")
flavorHistos[1].Draw("sameP0")
legend = TLegend(0.66,0.5,0.99,0.78)
legend.AddEntry(flavorHistos[0],"Pythia 8 (status==43,44,51,52,62)","LP")
legend.AddEntry(flavorHistos[1],"Pythia 8 (status == 71)","LP")
legend.SetTextSize(0.027)
legend.Draw()
c.SaveAs("flavdist_pythia8comparison_nocuts.png")
c.Clear()
