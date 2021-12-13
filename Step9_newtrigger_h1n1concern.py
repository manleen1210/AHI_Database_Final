# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 00:29:29 2021

@author: manle
"""

""" TRIGGER CODE """
delimiter $$

CREATE TRIGGER h1n1_concern_trigger BEFORE INSERT ON e2e.h1n1
FOR EACH ROW
BEGIN
IF NEW.h1n1_concern > 3 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'H1N1 concern should be a numerical value between 0 and 3. Please try again.';
END IF;
END; 

$$

""" CHECKING TRIGGER """
INSERT INTO h1n1 (h1n1_concern) 
    VALUES (4);

