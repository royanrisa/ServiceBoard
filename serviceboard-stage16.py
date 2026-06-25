# === Stage 16: Add argparse support for the most common commands ===
# Project: ServiceBoard
import argparse

def main():
    parser = argparse.ArgumentParser(description="ServiceBoard CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List all requests
    list_parser = subparsers.add_parser('list', help='List all service requests')
    list_parser.add_argument('--status', choices=['open', 'in_progress', 'resolved'], default=None, help='Filter by status')
    
    # Create new request
    create_parser = subparsers.add_parser('create', help='Create a new service request')
    create_parser.add_argument('--customer', required=True, help='Customer name or ID')
    create_parser.add_argument('--description', required=True, help='Issue description')
    create_parser.add_argument('--priority', choices=['low', 'medium', 'high'], default='medium', help='Priority level')
    create_parser.add_argument('--deadline', type=str, help='Deadline date (YYYY-MM-DD)')
    
    # Assign request to technician
    assign_parser = subparsers.add_parser('assign', help='Assign a request to a technician')
    assign_parser.add_argument('--id', required=True, help='Request ID')
    assign_parser.add_argument('--technician', required=True, help='Technician name or ID')
    
    # Update status
    update_parser = subparsers.add_parser('update', help='Update request status')
    update_parser.add_argument('--id', required=True, help='Request ID')
    update_parser.add_argument('--status', choices=['open', 'in_progress', 'resolved'], required=True, help='New status')
    
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    
    # TODO: Implement command logic here using global data store
    print(f"Command '{args.command}' executed with arguments: {vars(args)}")

if __name__ == '__main__':
    main()
