#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TicTacToe.py
#  
#  Copyright 2017 matt <matt@matt-P-6860FX>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import random



Board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]
Size = len(Board)
exitgame = False
newgame = False

def make_board():
		global Board
		Board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]


def print_board():
	print_row(1, Board[0], Board[1], Board[2], Board[3])
	print_row(2, Board[4], Board[5], Board[6], Board[7])
	print_row(3, Board[8], Board[9], Board[10], Board[11])
	print_row(4, Board[12], Board[13], Board[14], Board[15])
	return;
	
def print_row( rownum, w, x, y, z ):
	wChar = printBoardValAsChar(w);
	xChar = printBoardValAsChar(x);
	yChar = printBoardValAsChar(y);
	zChar = printBoardValAsChar(z);
	if(rownum == 1):
		print '\033[4m' + wChar + "|" + xChar + "|" + yChar + "|" + zChar + '\033[0m'
	elif(rownum == 2):
		print '\033[4m' + wChar +  "|" + xChar + "|" + yChar + "|" + zChar + '\033[0m'
	elif(rownum == 3):
		print '\033[4m' + wChar +  "|" + xChar + "|" + yChar + "|" + zChar + '\033[0m'
	elif(rownum == 4):
		print wChar +  "|" + xChar + "|" + yChar + "|" + zChar
	return;
	
def printBoardValAsChar( Val ):
	if( Val == 0):
		return ' '
	elif ( Val == 1):
		return 'X'
	elif (Val == 10):
		return '0'

def displayMenu():
	menuRetVal = 0
	while menuRetVal < 1 or menuRetVal > 2: 
		menuRetValString = input("\nTic Tac Toe: \n 1. Single Player \n 2. Multiplayer \n\n::")
		if(tryInt(menuRetValString)):
			menuRetVal = int(menuRetValString);
	return menuRetVal

def displayOnePlayerDifficultyMenu():
	menuRetVal = 0
	while menuRetVal < 1 or menuRetVal > 2: 
		menuRetValString = input("\nDifficulty: \n 1. Beginner \n 2. Advanced \n\n::")
		if(tryInt(menuRetValString)):
			menuRetVal = int(menuRetValString);
	return menuRetVal
	
def tryInt(aVal):
	try:
		int(aVal)
		return True;
	except ValueError:
		return False;
	
def displayOnePlayerWhoGoesFirst():
	menuRetVal = 0
	global whoGoesFirst
	while menuRetVal < 1 or menuRetVal > 2: 
		menuRetValString = input("\nWho goes first? \n 1. Player \n 2. Computer \n\n::")
		if(tryInt(menuRetValString)):
			menuRetVal = int(menuRetValString);
	return menuRetVal
	
def displayTwoPlayerWhoGoesFirst():
	menuRetVal = 0
	global whoGoesFirst
	while menuRetVal < 1 or menuRetVal > 2: 
		menuRetValString = input("\nWho goes first? \n 1. Player 1 \n 2. Player 2 \n\n::")
		if(tryInt(menuRetValString)):
			menuRetVal = int(menuRetValString);
	return menuRetVal	

def checkValidMove( location ):
	global Size
	if(location < 1):
		return False
	if(location > Size+1):
		return False
	if(Board[location - 1] > 0):
		return False
	else:
		return True;

def placeAtPosition(Location, currentPlayer):
	if(currentPlayer == 1):
		Board[Location-1] = 1
	else:
		Board[Location-1] = 10

def checkDiagonalWin(playerToCheck):
	if(Board[0] == playerToCheck and Board[5] == playerToCheck and Board[10] == playerToCheck and Board[15] == playerToCheck):
		return True
	elif(Board[3] == playerToCheck and Board[6] == playerToCheck and Board[9] == playerToCheck and Board[12] == playerToCheck):
		return True
	else:
		return False;

def checkVerticalWin(playerToCheck):
	for num in range(0, 4):
		if(Board[num + 0] == playerToCheck and Board[num + 4] == playerToCheck and Board[num + 8] == playerToCheck and Board[num + 12] == playerToCheck):
			return True
	return False

def checkHorizontalWin( playerToCheck ):
	for num in range(0, 4):
		if(Board[0 + (4*num)] == playerToCheck and Board[1 + (4*num)] == playerToCheck and Board[2 + (4*num)] == playerToCheck and Board[3 + (4*num)]  == playerToCheck):
			return True
	return False
						
def checkForWin( playerToCheck ):
	if(checkHorizontalWin(playerToCheck)):
		return True
	elif(checkVerticalWin(playerToCheck)):
		return True
	elif(checkDiagonalWin(playerToCheck)):
		return True
	else:
		return False

	

def randomComputerMove():
	val = random.randint(1, 16);
	while not checkValidMove(val):
		val = random.randint(1, 16);
	placeAtPosition(val, 2)
		
def doComputerMove():
	global atWhatDifficulty
	if (atWhatDifficulty == 1):
		randomComputerMove()
	elif (atWhatDifficulty == 2):
		bestComputerChoice()
	
def doPlayerOneMove():
	global newgame
	global exitgame
	PlayerResponse = raw_input("\nPlayer 1\n\nN: new game \nQ: quit game \nEnter a position[1-16]:");
	if(len(PlayerResponse) == 0):
		print "\n\nInvalid Command Length!\n\n"
		print_board()
		doPlayerOneMove()	
	elif(PlayerResponse == 'q' or PlayerResponse == 'Q'):
		exitgame = True
		return
	elif(PlayerResponse == 'n' or PlayerResponse == 'N'):
		newgame = True
		return
	else:
		if(tryInt(PlayerResponse)):
			PlayerLocation = int(PlayerResponse)
			if(checkValidMove(PlayerLocation)):
				placeAtPosition(PlayerLocation, 1)
			else:
				print "\n\nYou can't use that location!\n\n"
				print_board()
				doPlayerOneMove()
		else:
			print "\n\nInvalid Command!\n\n"
			print_board()
			doPlayerOneMove()
					
def doPlayerTwoMove():
	global newgame
	global exitgame
	PlayerResponse = raw_input("\nPlayer 2\n\nN: new game \nQ: quit game \nEnter a position[1-16]:");
	if(len(PlayerResponse) == 0):
		print "\n\nInvalid Command Length!\n\n"
		print_board()
		doPlayerTwoMove()
	elif(PlayerResponse == 'q' or PlayerResponse == 'Q'):
		exitgame = True
		return
	elif(PlayerResponse == 'n' or PlayerResponse == 'N'):
		newgame = True
		return
	else:
		if(tryInt(PlayerResponse)):
			PlayerLocation = int(PlayerResponse)
			if(checkValidMove(PlayerLocation)):
				placeAtPosition(PlayerLocation, 2)
			else:
				print "\n\nYou can't use that location!\n\n"
				print_board()
				doPlayerTwoMove()			
		else:
			print "\n\nInvalid Command!\n\n"
			print_board()
			doPlayerTwoMove()
			
def startGameOnePlayer( whoseTurn ):
	global newgame
	global exitgame
	print "\n\n"
	if(whoseTurn == 1): #Player 1
		print_board(); 
		doPlayerOneMove()
		if( not exitgame and not newgame):
			if(not checkForWin(1)):
				startGameOnePlayer(2)
			else:
				doPlayerOneWin()
	elif(whoseTurn == 2):
		if( not exitgame and not newgame):
			doComputerMove()
			if(not checkForWin(10)):
				startGameOnePlayer(1)
			else:
				doComputerWin()


def doComputerWin():
	print_board()
	print "\n\nToo bad, the computer won.\n\n"
		
def doPlayerOneWin():
	print_board()
	print "\n\nCongratulations Player 1!\n\n"

def doPlayerTwoWin():
	print_board()
	print "\n\nCongratulations Player 2!\n\n"

def startGameTwoPlayer( whoseTurn ):
	global exitgame
	global newgame
	print "\n\n"
	print_board();
	if(whoseTurn == 1): #Player 1			
		doPlayerOneMove()
		if(not exitgame and not newgame):
			if(not checkForWin(1)):
				startGameTwoPlayer(2)
			else:
				doPlayerOneWin()
	elif(whoseTurn == 2):
		doPlayerTwoMove()
		if(not exitgame and not newgame):
			if(not checkForWin(10)):
				startGameTwoPlayer(1)
			else:
				doPlayerTwoWin()
			
atWhatDifficulty = 1		
		

quads = [[0, 1, 2, 3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3, 6, 9, 12]]



def getQuadData(): # returns quad position amount as array
	returnArray = []
	for position in range(0, len(quads)): # does this return len as zero based?
		QuadCounter = 0 
		for element in range(0, 4):
			QuadCounter += Board[quads[position][element]]
		returnArray.append(QuadCounter)
	return returnArray

def bestComputerChoice():
	valData = getQuadData()
	
	position = checkForComputerPossibleWin(valData) #If I can win, I should do this first
	if(position != -1):
		placeAtPosition(position+1, 10) #+1 because of the -1 in place
	else:
		position = checkForPlayerPossibleWin(valData) #returns quad position So block the player!
		if(position != -1):
			placeAtPosition(position+1, 10);
			return
		else:
			randomComputerMove()



def checkForPlayerPossibleWin( quadData ):
	for number in range(0, len(quadData)):
		if(quadData[number] == 3):
			print "Player Win Possible at QuadData",quads[number] 
			for innernum in range(0, 4):
				print "Val At",Board[quads[number][innernum]] 
				if(Board[quads[number][innernum]] == 0):
					return quads[number][innernum]
	return -1

def checkForComputerPossibleWin(valData):
	for number in range(0, len(valData)):
		if(valData[number] == 30):
			for innernum in range(0, 4):
				if(Board[quads[number][innernum]] == 0):
					return quads[number][innernum]
	return -1	
	



def main(args):
	global atWhatDifficulty
	global exitgame
	global newgame
	random.seed()
	while not exitgame:
		menuRetVal = displayMenu()
		if(menuRetVal == 1):
			make_board();
			whoGoesFirst = displayOnePlayerWhoGoesFirst()
			atWhatDifficulty = displayOnePlayerDifficultyMenu()
			startGameOnePlayer(whoGoesFirst)
		if(menuRetVal == 2):
			make_board()
			whoGoesFirst = displayTwoPlayerWhoGoesFirst()
			startGameTwoPlayer(whoGoesFirst)
		newgame = False;
	return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
