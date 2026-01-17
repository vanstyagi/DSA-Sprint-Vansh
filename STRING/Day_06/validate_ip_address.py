def validIPAddress(self, queryIP):
        if not queryIP:
            return "Neither"
        if '.' in queryIP and ':' not in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
        
            for part in parts:
                if not part or len(part) > 3:
                    return "Neither"

                if not part.isdigit():
                    return "Neither"
 
                if len(part) > 1 and part[0] == '0':    
                    return "Neither"
 
                num = int(part)
                if num < 0 or num > 255:
                    return "Neither"
        
            return "IPv4"
    
        elif ':' in queryIP and '.' not in queryIP:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
            hex_digits = "0123456789abcdefABCDEF"
        
            for part in parts:
                if not part or len(part) > 4:
                    return "Neither"
                for char in part:
                    if char not in hex_digits:
                        return "Neither"
            return "IPv6"
    
        return "Neither"
        