#!/usr/bin/env python3

def main():
    """Get the token from the enviroment, and query for pods."""
    host = get_env('HOST')

    # The NAMESPACE env is provided by the Kuberntes DownwardAPI
    # https://docs.okd.io/latest/dev_guide/downward_api.html

    namespace = get_env('NAMESPACE')
    print("Host {}".format(host))
    print("Namespace {}".format(namespace))

if __name__ == "__main__":
    sys.exit(main())
