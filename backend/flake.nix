{
  description = "A flake to set up Python 3.12 in a project environment";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    {
      devShells.x86_64-linux.default =
        let
          pkgs = import nixpkgs { system = "x86_64-linux"; };
        in
        pkgs.mkShell {
          buildInputs = with pkgs; [
            python312 # Python 3.12
            python312Packages.pip # pip
            cargo
            rustc
            dotenv-cli
          ];

          # Optional: Define any shell hooks or additional environment variables
          shellHook = ''
            source .venv/bin/activate
          '';
        };
    };
}
